import os
from html import HTML

from MaudeMiner.core.database import db
from MaudeMiner.utils import update_progress
from MaudeMiner.core.models import *
from MaudeMiner.settings import DATA_PATH

INDEX_PATH = DATA_PATH + 'html/'
REPORT_PATH = DATA_PATH + 'html/reports/'

def run(args):
	# Ensure directories exist
	if not os.path.exists(REPORT_PATH):
		os.makedirs(REPORT_PATH)
	if not os.path.exists(INDEX_PATH):
		os.makedirs(INDEX_PATH)
	

	print "Querying..."
	session = db.get_session()
	# sql = " \
	# SELECT * \
	# FROM narratives, events \
	# limit 100"
	# r = db.execute_sql(sql, use_labels=True)

	# r = session.query(Event).limit(100).all()
	r = session.query(Event).join(Narrative).limit(100).all()

	print "Writing html for {0} reports...".format(len(r))
	# create index page
	index = HTML()
	ul = index.ul

	# for each report, add a link in the index and create a page
	for report in r:
		report_key = str(report[0].report_key)
		filename = 'reports/' + report_key + '.html'
		ul.li.a(report_key, href='{0}'.format(filename))
		create_page_for_report(report)

	path_name = INDEX_PATH + 'index.html'
	with open(path_name, 'w') as f:
		f.write(str(index))

	print "Done."



def create_page_for_report(report):
	page = HTML()
	table = page.table

	# loop through each table
	for model in report:
		columns = model.__dict__.keys()
		for col in columns:
			val = getattr(model, col)
			
			tr = table.tr
			tr.td(col.replace('_', ' '))
			tr.td(str(val))



	path_name = REPORT_PATH + str(report[0].report_key) + '.html'
	with open(path_name, 'w') as f:
		f.write(str(page))




def build_sql():
	sql = "SELECT "

	for t in [Event, Narrative, Device, DeviceProblem, Patient]:
		for col in t.__table__.columns:
			alias = str(col).replace('.', '_')
			sql += str(col) + " AS " + alias + ", \n"

	sql = sql[:-3] + " \n"

	sql += "FROM Events \
	LEFT JOIN Narratives ON Events.report_key = Narratives.report_key \
	LEFT JOIN Devices ON Events.report_key = Devices.report_key \
	LEFT JOIN DeviceProblems ON Events.report_key = DeviceProblems.report_key \
	LEFT JOIN Patients ON Events.report_key = Patients.report_key \
	ORDER BY Narratives.report_key ASC;"

	return sql



