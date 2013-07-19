import string
from nltk import wordpunct_tokenize
from sqlalchemy.sql.expression import ClauseElement

from MaudeMiner.database import db
from MaudeMiner.tokenizer import models as m
from MaudeMiner.utils import update_progress, strip_punctuation
from MaudeMiner.loader.utils import get_files_with_prefix, LINES_IN_CURRENT_FILE
from MaudeMiner.maude.models import Narrative
from MaudeMiner.settings import LINES_PER_DB_COMMIT, TXTS_PATH


def get_or_create(session, model, defaults=None, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance, False
    else:
        params = dict((k, v) for k, v in kwargs.iteritems() if not isinstance(v, ClauseElement))
        params.update(defaults)
        instance = model(**params)
        session.add(instance)
        return instance, True

def load(args):
	db.create_tables(["Words"])

	print " === Building Word Bank === "
	session = db.get_session()

	num_results = session.query(Narrative).count()

	offset = 0
	batch_size = 10000

	dictionary = {}

	while offset < num_results:
		# get a batch of narratives
		for narrative in session.query(Narrative).limit(batch_size).offset(offset):
			tokens = wordpunct_tokenize(narrative.text)

			# load dictionary from each narrative in the batch
			for token in tokens:
				if token not in dictionary:
					dictionary[token] = 1
				else:
					dictionary[token] += 1

		# for key, val in dictionary.items():
			# print key, val

		# print len(dictionary)
		# dictionary.clear()
		# offset += batch_size
		# continue

		for word, freq in dictionary.items():
			instance, isNew = get_or_create(db.session, m.Word, defaults={"frequency": 0}, word=word)
			if isNew:
				instance.frequency = freq
			else:
				instance.frequency += freq

		db.commit()

		# # get list of matching word objects
		# q_words = session.query(m.Word).filter(m.Word.word.in_(dictionary.keys())).all()

		# # update existing words in database
		# print "Updating", len(q_words)
		# for word in q_words:
		# 	word.frequency += dictionary[word.word]
		# 	del dictionary[word.word]

		# # create new words in database
		# print "Creating", len(dictionary.keys())
		# for word, freq in dictionary.items():
		# 	instance = m.Word(word, freq)
		# 	db.save(instance, commit=False)
		# # db.commit()

		# prepare for next batch
		dictionary.clear()
		offset += batch_size
		update_progress("Processed: ", offset, num_results)
	
	# final commit
	db.commit()
	print "\nDone." # end update progress line

