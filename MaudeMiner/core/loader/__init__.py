import os
import sys
import fileinput
from MaudeMiner.utils import list_table_options
from MaudeMiner.core.database import db

from MaudeMiner.core.loader import events
from MaudeMiner.core.loader import narratives
from MaudeMiner.core.loader import devices
from MaudeMiner.core.loader import device_problems
from MaudeMiner.core.loader import device_problem_codes
from MaudeMiner.core.loader import patients


LINES_PER_COMMIT = 50000

def run(args=None):
	if not args or len(args) == 0:
		print "Load what?"
		list_table_options()
		return

	if "all" in args:
		args = db.get_table_names()

	if "Events" in args:
		events.load()
	if "Narratives" in args:
		if "debug" in args:
			narratives.load(1)
		else:
			narratives.load()
	if "Devices" in args:
		devices.load()
	if "DeviceProblems" in args:
		device_problems.load()
	if "DeviceProblemCodes" in args:
		device_problem_codes.load()
	if "Patients" in args:
		patients.load()
