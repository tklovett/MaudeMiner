from MaudeMiner.database import db
from MaudeMiner.querier.results import process_results


def execute_sql(sql):
	print "Querying database..."
	r = db.execute_sql(sql)
	process_results(r, query=sql)
