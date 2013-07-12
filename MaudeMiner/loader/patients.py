from MaudeMiner.database import db
from MaudeMiner.maude.models import Patient
from MaudeMiner.utils import update_progress
from MaudeMiner.loader.utils import *
from MaudeMiner.settings import LINES_PER_DB_COMMIT


EXPECTED_NUMBER_OF_FIELDS = 5


def load():
	# ensure tables exists
	db.create_tables(["Patients"])

	print " === Loading Patients === "

	files = get_files_with_prefix("patient", excludes=['patientAdd', 'patientChange'])

	for line in files:
		v = split_fields(line)
		if len(v) != EXPECTED_NUMBER_OF_FIELDS:
			continue

		patient = Patient()
		patient.report_key                = v[0]
		patient.patient_sequence_number   = v[1]
		patient.date_received             = v[2]
		patient.sequence_number_treatment = v[3]
		patient.sequence_number_outcome   = v[4]
		db.save(patient, commit=False)


		if files.lineno() % 1000 == 0:
			update_progress("Loaded: ", files.lineno(), LINES_IN_CURRENT_FILE[0])
			if files.lineno() % LINES_PER_DB_COMMIT == 0:
				db.commit()

	db.commit()
	print "\n # Done # \n"