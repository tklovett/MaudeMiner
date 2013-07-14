import nltk
import string
from MaudeMiner.database import db
from MaudeMiner.tokenizer import models
from MaudeMiner.utils import update_progress
from MaudeMiner.loader.utils import get_files_with_prefix, LINES_IN_CURRENT_FILE
from MaudeMiner.maude.models import Narrative
from MaudeMiner.settings import LINES_PER_DB_COMMIT, TXTS_PATH

nouns_verbs_adjectives = []


def load_file():
	db.create_tables(["Contains_Token", "Tokens", "Words"])

	print " === Building Word List === "
	files = get_files_with_prefix("foitext", excludes=["foitextChange", 'foitextAdd'])
	to = " " * len(string.punctuation)
	trans = string.maketrans(string.punctuation, to)
	for line in files:
		pos = line.rfind('|')
		text = line[pos:].translate(trans)
		words = text.split()
		
		for w in words:
			word = models.Word(w)
			db.save(word, suppress_errors=True)

		if files.filelineno() % 100 == 0:
			update_progress("Processed: ", files.filelineno(), LINES_IN_CURRENT_FILE[0])

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

