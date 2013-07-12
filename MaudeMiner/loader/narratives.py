from MaudeMiner.database import db
from MaudeMiner.maude.models import Narrative
from MaudeMiner.utils import update_progress
from MaudeMiner.loader.utils import *
from MaudeMiner.settings import LINES_PER_DB_COMMIT


EXPECTED_NUMBER_OF_FIELDS = 6


def load():
	# ensure tables exists
	db.create_tables(["Narratives"])

	print " === Loading Narratives === "

	files = get_files_with_prefix("foitext", excludes=["foitextChange", 'foitextAdd'])

	for line in files:
		v = split_fields(line)
		if len(v) != EXPECTED_NUMBER_OF_FIELDS:
			continue

		narrative = Narrative()
		narrative.report_key              = v[0]
		narrative.text_key                = v[1]
		narrative.text_type_code          = v[2]
		narrative.patient_sequence_number = v[3]
		narrative.date_report             = v[4]
		narrative.text                    = v[5]
		db.save(narrative, commit=False)


		if files.lineno() % 1000 == 0:
			update_progress("Loaded: ", files.lineno(), LINES_IN_CURRENT_FILE[0])
			if files.lineno() % LINES_PER_DB_COMMIT == 0:
				db.commit()

	db.commit()
	print "\n # Done # \n"