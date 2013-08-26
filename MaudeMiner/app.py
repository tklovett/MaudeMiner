import sys
from MaudeMiner.core.database import db
from MaudeMiner.core import downloader
from MaudeMiner.core import loader
from MaudeMiner.utils import list_table_options
from MaudeMiner import interactive
from MaudeMiner.settings import INSTALLED_MODULES


# # Import installed modules
# def import_module(name):
# 	m = __import__(name)
# 	for n in name.split(".")[1:]:
# 		m = getattr(m, n)
# 	return m

# modules = {}
# for module in INSTALLED_MODULES:
# 	modules[module] = import_module("MaudeMiner." + module)


# commands = {}
# for m in modules:
# 	try:
# 		from m import commands
# 		for c in m + "_commands":
# 			commands[c] = c
# 			print c
# 	except:
# 		print "Module " + m + " has no commands registered. You won't be able to access this module using MaudeMiner!"



import cleanser
import tokenizer
import querier
import html_generator

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
			text = raw_input("|- python> ")
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
	"html":   html_generator.run,
}

