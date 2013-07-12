import sys
from MaudeMiner.database import db

def update_progress(prefix, complete, total):
	if total == None or total == 0:
		sys.stdout.write('\r{0}\'{1}\'%'.format(prefix, total))
		sys.stdout.flush()
		return

	progress = '\r{0}{1:.2f}%'.format(prefix, complete / float(total) * 100)
	sys.stdout.write(progress)

	if complete == total:
		sys.stdout.write("\n")

	sys.stdout.flush()

def list_table_options(prefix=" "):
	print prefix + "all (recommended)"
	for t in db.get_table_names():
		print prefix + t

