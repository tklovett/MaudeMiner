import os
from datetime import datetime
from MaudeMiner.settings import DATA_PATH



def process_results(result, title="", doWrite=True, query=""):
	"""write the results of the last SQL query to disk and to screen"""

	if not result or not result.returns_rows:
		print "-> 0 records returned"
		print result
		return

	doPrint = True

	# get column names
	cols = result.keys()

	# build template format string
	template = ""
	for i in range(len(cols)):
		template += "{%s:40}" % i
	template = template.replace("}{", "}|{")

	# open output file
	if doWrite:
		results_dir = DATA_PATH + "query_results/"
		if not os.path.exists(results_dir):
			os.makedirs(results_dir)

		now = datetime.now().strftime("%Y_%m_%d__%I_%M_%p")
		filename = results_dir + "query_results_" + now
		
		txt = open(filename+".txt", 'w')
		csv = open(filename+".csv", 'w')

		# print query
		txt.write(query + "\n")
		txt.write("=" * len(query) + "\n")
		csv.write(query + "\n")

		# print header
		txt.write(template.format(*tuple(cols)) + "\n") # header
		txt.write("-"*41*len(cols) + "\n")
		csv.write('|'.join(cols) + "\n")

	# print records
	numRecs = 0
	for row in result:
		# ask user if they want ot stop printing after 100 records
		if numRecs == 100:
			i = raw_input("100 records printed. Continue printing records? (y/N) ")
			if i.lower() not in ["y", "yes"]:
				doPrint = False
		
		if doPrint:
			screen_write_row(row, title)

		if doWrite:
			txt_write_row(txt, template, row)
			csv_write_row(csv, row)

		# count records returned
		numRecs += 1

	# show number of records returned
	print "-> %s records returned" % numRecs
	if doWrite:
		txt.write(	"-> %s records returned" % numRecs)

	if doWrite:
		txt.flush()
		txt.close()

def screen_write_row(row, title=''):
	print "=" * 3 + title + "=" * (77-len(title))
	for key in row.keys():
		print key + ":"
		print "-" * (len(key)+1)
		print row[key]
		print ""
	print "=" * 80

def txt_write_row(txt_file, template, row):
	txt_file.write(template.format(*row) + "\n")

def csv_write_row(csv_file, row):
	csv_file.write('|'.join(map(str,row)) + "\n")