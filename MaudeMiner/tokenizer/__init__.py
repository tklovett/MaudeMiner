import nltk
from MaudeMiner.database import db
from MaudeMiner.tokenizer import models
from MaudeMiner.utils import update_progress
from MaudeMiner.loader.utils import get_files_with_prefix
from MaudeMiner.maude.models import Narrative
from MaudeMiner.settings import LINES_PER_DB_COMMIT, TXTS_PATH

nouns_verbs_adjectives = []


def load_file():
	files = get_files_with_prefix("foitext", excludes=["foitextChange", 'foitextAdd'])

	for line in files:
		import string
		text = line.translate(dict.fromkeys(map(ord, string.punctuation), u' '))
		print text

def load():
	db.create_tables(["Contains_Token", "Tokens", "Words"])

	print " === Tokenizing === "
	session = db.get_session()
	q = session.query(Narrative)
	# q = q.limit(100)

	num_results = q.count()

	offset = 0
	batch_size = 100
	while offset < num_results:
		for narrative in q.limit(batch_size).offset(offset):
			tokens = nltk.word_tokenize(narrative.text)
			for token in tokens:
				word = models.Word(token)
				db.save(word, commit=False)

		offset += batch_size
		update_progress("Processed: ", offset, num_results)
		db.commit()
	
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

		elif "loadfile" in words:
			load_file()

		elif "exit" in words:
			return
		elif words[0] == "":
			pass
		else:
			print "huh?"

