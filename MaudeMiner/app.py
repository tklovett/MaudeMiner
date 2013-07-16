from MaudeMiner.database import db
from MaudeMiner import interactive
from utils import list_table_options
import query as q
import cleanser
import downloader
import loader
import tokenizer
import querier


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
	interactive.start("module", 0, commands)

	# if we've returned from the top level interactive,
	# then quit the program
	db.disconnect()
	exit()

commands = {
	"download": downloader.run,
	"load":      loader.run,
	"create":   create_tables,
	"drop":     drop_tables,
	"count":    count_records,
	"switchdb":  switch_db,
	"shell":     shell,
	"cleanse":  cleanser.run,
	"tokenizer": tokenizer.run,
	"querier":   querier.run,
}

