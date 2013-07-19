import nltk
import string
from MaudeMiner import interactive
from MaudeMiner.database import db
from MaudeMiner.tokenizer import models, words
from MaudeMiner.utils import update_progress, strip_punctuation
from MaudeMiner.loader.utils import get_files_with_prefix, LINES_IN_CURRENT_FILE
from MaudeMiner.maude.models import Narrative
from MaudeMiner.settings import LINES_PER_DB_COMMIT, TXTS_PATH


def removeNonAscii(s):
	return "".join(i for i in s if ord(i) < 128)

def removePunctuation(s):
	# TODO replace with ' '
	return s.translate(None, string.punctuation)

def load_file():
	db.create_tables(["Contains_Token", "Tokens", "Words"])

	print " === Building Word List === "
	files = get_files_with_prefix("foitext", excludes=["foitextChange", 'foitextAdd'])
	
	batch = set()

	for line in files:
		pos = line.rfind('|')

		text = removeNonAscii(line[pos+1:])
		text = strip_punctuation(text, replace=' ')
		text = text.lower()
		# print text

		batch |= set(unicode(text).split())

		if len(batch) > 100000:
			for w in batch:
				db.save(models.Word(w), commit=False)
			db.commit()
			batch.clear()

		if files.filelineno() % 1000 == 0:
			update_progress("Processed: ", files.filelineno(), LINES_IN_CURRENT_FILE[0])

	print "\nDone."

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
	interactive.start("tokenizer", 1, commands)

commands = {
	"load": load,
	"loadfile": load_file,
	"words": words.load,
}
