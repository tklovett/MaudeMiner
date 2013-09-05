from urllib2 import urlopen
from zipfile import ZipFile
from bs4 import BeautifulSoup
import os
import sys

from MaudeMiner.settings import MAUDE_DATA_ORIGIN, DATA_PATH, ZIPS_PATH, TXTS_PATH
from MaudeMiner.utils import update_progress

def get_data_urls():
	sys.stdout.write("Scraping MAUDE website for data urls: ")
	sys.stdout.flush()
	urls = []
	soup = BeautifulSoup(str(urlopen(MAUDE_DATA_ORIGIN).read()), "html5lib")
	# search page for anchor tags with links to zip files
	for a in soup.findAll('a'):
		if a.has_attr('href') and ".zip" in a['href']:
			urls.append(a['href'])
	sys.stdout.write("OK - found %i URLs\n" % len(urls))
	sys.stdout.flush()
	return urls

def prepare_directory():
	sys.stdout.write("Preparing data directory: ")
	sys.stdout.flush()

	# make directories if they dont exist
	if not os.path.exists(ZIPS_PATH):
		os.makedirs(ZIPS_PATH)
	if not os.path.exists(TXTS_PATH):
		os.makedirs(TXTS_PATH)

	# remove existing data files
	for file in os.listdir(ZIPS_PATH):
		os.remove(ZIPS_PATH+file)
	for file in os.listdir(TXTS_PATH):
		os.remove(TXTS_PATH+file)

	sys.stdout.write("OK - %s\n" % DATA_PATH)
	sys.stdout.flush()

def download_data(urls):
	message = "Downloading data: "
	num_complete = 0
	update_progress(message, 0, len(urls))

	for url in urls:
		# get file name
		begin = url.rfind("/")+1
		zip_filename = url[begin:]
		with open(ZIPS_PATH+zip_filename, 'wb') as zipfile:
			zipfile.write(urlopen(url).read())
		num_complete += 1
		update_progress(message, num_complete, len(urls))

	print "\r{0}OK - {1}".format(message, ZIPS_PATH)
	return num_complete

def extract_data(num_files):
	message = "Extracting data:  "
	num_complete = 0
	update_progress(message, 0, num_files)

	for file in os.listdir(ZIPS_PATH):
		zip_data = ZipFile(ZIPS_PATH+file, 'r').extractall(TXTS_PATH)
		num_complete += 1
		update_progress(message, num_complete, num_files)

	print "\r{0}OK - {1}".format(message, TXTS_PATH)

def run(args=None):
	print "=== Downloading Data ==="
	prepare_directory()
	zip_urls  = get_data_urls()
	num_files = download_data(zip_urls)
	extract_data(num_files)
	print "Done!"

if __name__ == "__main__":
	run()