from MaudeMiner.core.database import db
from MaudeMiner import interactive
from MaudeMiner.querier.results import process_results


def run(args):
	interactive.start("sqlite", 2, process_input=process_sql)

def process_sql(text):
	# append ';' if the user forgot it
	if not text.endswith(";"):
		text += ";"
	execute_sql(text)


def execute_sql(sql):
	print "Querying database..."
	r = db.execute_sql(sql)
	process_results(r, query=sql)
