import os
import fileinput
from MaudeMiner.settings import TXTS_PATH

# This is a hack to give me an immutable integer.
# This lets me import a reference instead of just he integer
LINES_IN_CURRENT_FILE = [None]

def file_openhook(filename, mode):
	# determine number of lines in this file
	infile = open(filename, mode)
	LINES_IN_CURRENT_FILE[0] = get_number_of_lines(infile)
	print "\nFile: {0}\tMode: {1}\tLines: {2}".format(filename, mode, LINES_IN_CURRENT_FILE[0])
	infile.close()

	return open(filename, mode)

def get_files_with_prefix(prefix, excludes=[]):
	# get all data files
	file_list = []
	for f in os.listdir(TXTS_PATH):
		# check for Patient file
		if not f.startswith(prefix):
			continue
		if not f.endswith(".txt"):
			continue
		if f.split('.')[0] in excludes:
			continue
		file_list.append(TXTS_PATH + f)

	print "Number of files: {0}".format(len(file_list))

	return fileinput.input(file_list, mode='rU', openhook=file_openhook)

def split_fields(line):
	# convert all white space to spaces, remove
	# newlines and split by pipes
	line = unicode(line, errors="ignore")
	return " ".join(line.split()).split('|')

def get_number_of_lines(infile):
	'''
	fancy line counting algorithm by Ryan Ginstrom via stackoverflow
	http://stackoverflow.com/questions/845058/how-to-get-line-count-cheaply-in-python
	http://stackoverflow.com/users/10658/ryan-ginstrom
	'''
	lines = 0
	buf_size = 1024 * 1024
	read_f = infile.read # loop optimization

	buf = read_f(buf_size)
	while buf:
		lines += buf.count('\n')
		buf = read_f(buf_size)

	return lines