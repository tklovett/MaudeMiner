import string
from itertools import permutations
from MaudeMiner.querier.sql import execute_sql

def run():
	print "Enter the list of comma-separate keywords to search for at the prompt."
	text = raw_input("keywords> ")

	# strip whitespace and split by commas to get list of keywords
	keywords = text.translate(None, string.whitespace).split(',')

	sql = "SELECT * FROM Narratives WHERE text LIKE \'"

	# use all permutations of the keywords
	phrases = []
	for permutation in permutations(keywords, len(keywords)):
		phrase = "%"
		for keyword in permutation:
			phrase += "{0}%".format(keyword)
		phrases.append(phrase)
	sql += " OR ".join(phrases) + "\';"

	execute_sql(sql)