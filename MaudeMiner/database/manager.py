import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError, SQLAlchemyError, OperationalError

from MaudeMiner.settings import DATA_PATH, DATABASE_PATH, DATABASE_NAME
from MaudeMiner.database.base import base


class DatabaseManager:
	engine     = None
	session    = None
	connection = None

	def __init__(self):
		self.set_db(DATABASE_NAME)

	def set_db(self, name):
		if not name or name == "":
			raise RuntimeError('No database name provided to function set_db')

		self.disconnect()

		# create folders for database file if necessary
		if not os.path.exists(DATABASE_PATH):
			os.makedirs(DATABASE_PATH)

		# build database filename
		db_filename = 'sqlite:///{0}{1}.db'.format(DATABASE_PATH, name)

		self.engine     = create_engine(db_filename, echo=False)
		self.session    = sessionmaker(bind=self.engine)()
		self.connection = self.engine.connect()
		print "Connected to " + db_filename

	def get_session(self):
		return sessionmaker(bind=self.engine)()

	def disconnect(self):
		if self.connection != None:
			self.connection.close()
		if self.session != None:
			self.session.commit()
			self.session.close()

	def save(self, thing, commit=True, suppress_errors=False):
		ok = True
		try:
			self.session.add(thing)
			if commit:
				self.session.commit()
		except IntegrityError as e:
			if not suppress_errors:
				print "IntegrityError:"
				print "\t%s" % e.orig.args
			ok = False
		except SQLAlchemyError as e:
			if not suppress_errors:
				print "SQLAlchemyError:"
				print "\t%s" % e
			ok = False
		except:
			if not suppress_errors:
				print "Could not save item:"
				print "\t%s" % sys.exc_info()[0]
			ok = False

		if not ok:
			self.session.rollback()
			return False

		return True

	def flush(self):
		self.session.flush()

	def commit(self, verbose=False):
		ok = True
		try:
			self.session.commit()
		except IntegrityError as e:
			print "IntegrityError:"
			print "\t%s" % e.orig.args
			ok = False
		except SQLAlchemyError as e:
			print "SQLAlchemyError:"
			print "\t%s" % e
			ok = False
		except:
			print "Error:"
			print "\t%s" % sys.exc_info()[0]
			ok = False

		if not ok:
			print "Could not commit block!! DATA LOST."
			self.session.rollback()
			return False

		return True

	def __get_table_objects(self, table_names):
		# make list of table objects
		table_list = base.metadata.sorted_tables
		table_list_cpy = base.metadata.sorted_tables
		for t in table_list_cpy:
			if str(t) not in table_names:
				table_list.remove(t)
		return table_list

	def get_table_names(self):
		return base.metadata.tables.keys()

	def validate_table_names(self, tables):
		valid_tables = [x for x in tables if self.has_table(x)]

		for t in tables:
			if not self.has_table(t):
				print "Invalid table name: " + t

		return valid_tables

	def create_tables(self, tables):
		if "all" in tables:
			valid_tables = self.get_table_names()
		else:
			valid_tables = self.validate_table_names(tables)

		if len(valid_tables) == 0:
			return

		print " === Creating Table(s) === "
		for t in valid_tables:
			print "  " + str(t)

		table_objects = self.__get_table_objects(valid_tables)
		base.metadata.create_all(self.engine, table_objects)
		print "Done."

	def drop_tables(self, tables):
		if "all" in tables:
			valid_tables = self.get_table_names()
		else:
			valid_tables = self.validate_table_names(tables)

		if len(tables) == 0:
			return

		print "Are you sure you want to drop the following tables?"
		for t in valid_tables:
			print "  " + t
		if raw_input("All data will be lost. Operation may take a few minutes. (y/N) ") != "y":
			return

		table_objects = self.__get_table_objects(valid_tables)
		base.metadata.drop_all(self.engine, table_objects)

	def has_table(self, name):
		return name in base.metadata.tables.keys()

	def num_records_in_table(self, table):
		if not self.has_table(table):
			print "Invalid table name: " + table
			return

		table_object = self.__get_table_objects([table])[0]

		try:
			return self.session.query(table_object).count()
		except:
			print "Couldn't get count. Has the %s table been created?" % table

	def execute_sql(self, sql):
		try:
			result = self.connection.execute(sql)
		except OperationalError as e:
			print e
			return []
		except:
			print "Could not execute SQL"
			return []

		return result
