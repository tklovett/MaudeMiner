import nltk
from MaudeMiner.database import db
from MaudeMiner.maude.models import Narrative
from MaudeMiner.tokenizer import models

nouns_verbs_adjectives = []

def load():
	db.create_tables(["Contains_Token", "Tokens"])

	session = db.get_session()
	q = session.query(Narrative).filter()
	q = q.limit(10)

	for narrative in q:
		print narrative.text
		tokens = nltk.word_tokenize(narrative.text)
		token = models.Token()
		pos    = nltk.pos_tag(tokens)
		# print pos
		for token in pos:
			print token[1]





def run(args=None):

	while (True):
		cmd = raw_input("tokenizer> ")
		words = cmd.split(' ')

		if "clear" in words:
			db.drop_tables(["Contains_Token", "Tokens"])

		elif "load" in words:
			load()

		elif "exit" in words:
			return
		elif words[0] == "":
			pass
		else:
			print "huh?"

