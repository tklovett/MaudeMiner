from MaudeMiner.database import db
from MaudeMiner.maude.models import DeviceProblemCode
from MaudeMiner.utils import update_progress
from MaudeMiner.loader.utils import *

EXPECTED_NUMBER_OF_FIELDS = 2

def load():
	# ensure table exists
	db.create_tables(["DeviceProblemCodes"])

	print " === Loading Device Problem Codes === "

	files = get_files_with_prefix("deviceproblemcodes")

	for line in files:
		v = split_fields(line)
		if len(v) != EXPECTED_NUMBER_OF_FIELDS:
			continue

		dpc = DeviceProblemCode()
		dpc.code        = v[0]
		dpc.description = v[1]
		db.save(dpc, commit=False)

		# don't bother to update progress, there's only ~1000 records

	db.commit()
	print " # Done # \n"