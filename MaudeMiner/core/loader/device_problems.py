from MaudeMiner.core.database import db
from MaudeMiner.core.models import DeviceProblem
from MaudeMiner.utils import update_progress
from MaudeMiner.core.loader.utils import *
from MaudeMiner.settings import LINES_PER_DB_COMMIT


EXPECTED_NUMBER_OF_FIELDS = 2


def load():
	# ensure tables exists
	db.create_tables(["DeviceProblems"])

	print " === Loading Device Problems === "

	files = get_files_with_prefix("foidevproblem")

	for line in files:
		v = split_fields(line)
		if len(v) != EXPECTED_NUMBER_OF_FIELDS:
			continue

		problem = DeviceProblem()
		problem.report_key          = v[0]
		problem.code = v[1]
		db.save(problem, commit=False)


		if files.filelineno() % 1000 == 0:
			update_progress("Loaded: ", files.filelineno(), LINES_IN_CURRENT_FILE[0])
			if files.filelineno() % LINES_PER_DB_COMMIT == 0:
				db.commit()

	db.commit()
	print "\n # Done # \n"