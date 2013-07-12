from MaudeMiner.database import db
from utils import list_table_options
import query as q
import cleanser
import downloader
import loader
import tokenizer


def __exit__():
	db.disconnect()

def switch_db(args):
	if len(args) == 0:
		print "Usage is 'switchdb <db_name>'"
		return
	db.set_db(args[0])

def quit(args):
	db.disconnect()
	exit()

def print_help(args):
	print "Usage: <command> <arg1> <arg2> ..."
	print "Available commands:"
	for cmd in commands:
		print "\t" + cmd

def drop_tables(args):
	if len(args) == 0:
		print "Drop what?"
		list_table_options()
	else:
		db.drop_tables(args)

def create_tables(args):
	if len(args) == 0:
		print "Create what?"
		list_table_options()
	else:
		db.create_tables(args)

def count_records(args):
	if len(args) == 0:
		print "Count what?"
		list_table_options()
		return

	if "all" in args:
		args = db.get_table_names()

	for table in args:
		count = db.num_records_in_table(table)
		if count != None:
			print '{0:20s} {1:10d}'.format(table, count)


#####################
# Enter query modes #
#####################
def sql(args):
	q.raw_sql_mode(db)
def query(args):
	if len(args) != 1:
		print "Usage: query <table>"
		return
	q.build_query(db, args[0])


######################
# Enter Python shell #
######################
def shell(args):
	''' A simple Python Shell '''
	while True:
		try:
			text = raw_input(">>> ")
			if text == "exit":
				return
			print eval(text)
		except SyntaxError as e:
			print e
		except NameError as e:
			print e



def run():	
	while (True):
		cmd = raw_input("> ")
		words = cmd.split(' ')
		if words[0] in commands:
			commands[words[0]](words[1:])
		elif words[0] == "":
			pass
		else:
			print "Command not recognized. Enter \"help\" for a list of commands"


commands = {
	"cleanse":  cleanser.run,
	"count":    count_records,
	"create":   create_tables,
	"download": downloader.run,
	"drop":     drop_tables,
	"exit":     quit,
	"help":     print_help,
	"load":     loader.run,
	"query":    query,
	"shell":    shell,
	"sql":      sql,
	"switchdb": switch_db,
	"tokenizer": tokenizer.run,
}

