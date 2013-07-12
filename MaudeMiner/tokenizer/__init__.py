import nltk
from MaudeMiner.database import db
from MaudeMiner.utils import update_progress
from MaudeMiner.settings import LINES_PER_DB_COMMIT
from MaudeMiner.maude.models import Narrative
from MaudeMiner.tokenizer import models

nouns_verbs_adjectives = []

def load():
	db.create_tables(["Contains_Token", "Tokens", "Words"])

	session = db.get_session()
	q = session.query(Narrative).filter()
	# q = q.limit(100)

	num_results = q.count()

	i = 0
	for narrative in q:
		tokens = nltk.word_tokenize(narrative.text)
		for token in tokens:
				word = models.Word(token)
				db.save(word, commit=False)

		if i % LINES_PER_DB_COMMIT == 0:
			update_progress("Processed: ", i, num_results)
			db.commit()
		
		i += 1
	
	# final commit
	db.commit()
	print "\nDone." # end update progress line
		





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

