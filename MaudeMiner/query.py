import os
from MaudeMiner.database import db
from MaudeMiner.settings import DATA_PATH
from MaudeMiner.querier.results import process_results
from datetime import datetime
from sqlalchemy.exc import InvalidRequestError

class Query:
	__tables = []
	__limit = None
	__distinct = False

	def __init__(self, table):
		model = db.get_model_from_table_name(table)

		if model == None:
			raise Exception('Invalid table name')

		self.session = db.get_session()
		self.q = self.session.query(model)
		self.__tables.append(name)

	def __repr__(self):
		return "===\n%s\n===" % self.q.statement

	def get(self):
		return self.q.all()

	def set_distinct(self):
		__distinct = True
		self.q.distinct()

	def join(self, name=None, join_on=None, where=None, having=None):
		name = raw_input("Table: ")

		if not db.has_table(name):
			print "Invalid table name: " + name
			return

		if join_on == None:
			on = raw_input("On: ")

		try:
			self.q = self.q.join(name)
			self.__tables.append(name)
		except InvalidRequestError as e:
			print e

	def limit(self, number):
		self.__limit = number
		self.q = self.q.limit(number)




def __update_tables(action, tables):
	for t in tables:
		if db.isValidTable(t):
			if action == "add" and t not in __query_tables:
				__query_tables.append(t)
			elif action == "rm" and t in __query_tables:
				__query_tables.remove(t)
			else:
				print "Usage: tables [add|rm] <table1> <table2> ..."
		else:
			print "Invalid table name"

def __update_limit(limit):
	__query_limit = limit
	print __query_limit

def __get_records(db):
	sql = "SELECT * FROM"
	for table in __query_tables:
		sql += " " + table

	# limit
	if __query_limit != None:
		sql += " LIMIT " + __query_limit

	sql += ";"
	r = db.execute_sql(sql)
	process_results(r, "", doWrite=False)
	process_results(r)


def raw_sql_mode(db):
	while (1):
		sql = raw_input("sqlite> ")
		if sql in ["quit", "q", "exit"]:
			return
		if sql == "":
			continue
		if not sql.endswith(";"):
			sql += ";"

		r = db.execute_sql(sql)

		if r and r.returns_rows:
			process_results(r, query=sql)
		else:
			print "-> 0 records returned"

def build_query(db, name):
	model = db.get_model(name)
	query = Query(model)
	while (1):
		print query

		r = raw_input("query> ")
		words = r.split()
		if len(words) == 0:
			continue

		if words[0] == "join":
			query.join()

		elif words[0] == "limit":
			query.limit(words[1])

		elif words[0] == "get":
			process_results(query.get(), "", doWrite=False)

		elif words[0] == "clear":
			query = Query(name)

		elif words[0] == "exit":
			return

