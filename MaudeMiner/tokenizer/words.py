import string
from nltk import wordpunct_tokenize
from sqlalchemy.sql.expression import ClauseElement

from MaudeMiner.core.database import db
from MaudeMiner.tokenizer import models as m
from MaudeMiner.utils import update_progress, strip_punctuation
from MaudeMiner.loader.utils import get_files_with_prefix, LINES_IN_CURRENT_FILE
from MaudeMiner.core.models import Narrative
from MaudeMiner.settings import LINES_PER_DB_COMMIT, TXTS_PATH


def get_or_create(session, model, defaults=None, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance, False
    else:
        params = dict((k, v) for k, v in kwargs.iteritems() if not isinstance(v, ClauseElement))
        # params.update(defaults)
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

	word_frequencies = {}

	while offset < num_results:
		# get a batch of narratives
		for narrative in session.query(Narrative).limit(batch_size).offset(offset):
			tokens = wordpunct_tokenize(narrative.text)

			# load word_frequencies from each narrative in the batch
			for token in tokens:
				if token not in word_frequencies:
					word_frequencies[token] = 1
				else:
					word_frequencies[token] += 1

		# get or create each word in word_frequencies
		for word, freq in word_frequencies.items():
			instance, isNew = get_or_create(db.session, m.Word, word=word)
			if isNew:
				instance.frequency = freq
			else:
				instance.frequency += freq

		db.commit()

		# prepare for next batch
		word_frequencies.clear()
		offset += batch_size
		update_progress("Processed: ", offset, num_results)
	
	# final commit
	db.commit()
	print "\nDone." # end update progress line

