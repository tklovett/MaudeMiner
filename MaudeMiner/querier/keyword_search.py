import string
from itertools import permutations
from MaudeMiner.querier.sql import execute_sql

def run(args):
	print "Enter the list of comma-separated keywords to search for at the prompt."
	text = raw_input("keywords> ")

	# strip whitespace and split by commas to get list of keywords
	# keywords = text.translate(None, string.whitespace).split(',')
	keywords = [word.strip() for word in text.split(',')]

	sql = "SELECT * FROM Narratives WHERE "

	# use all permutations of the keywords
	phrases = []
	for permutation in permutations(keywords, len(keywords)):
		phrase = "text LIKE \'%"
		for keyword in permutation:
			phrase += "{0}%".format(keyword)
		phrase += "\'"
		phrases.append(phrase)
	
	sql += " OR ".join(phrases) + ";"

	execute_sql(sql)