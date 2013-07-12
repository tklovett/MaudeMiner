import os
import sys
import fileinput
from MaudeMiner.utils import list_table_options
from MaudeMiner.database import db

from MaudeMiner.loader import events
from MaudeMiner.loader import narratives
from MaudeMiner.loader import devices
from MaudeMiner.loader import device_problems
from MaudeMiner.loader import device_problem_codes
from MaudeMiner.loader import patients


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
		narratives.load()
	if "Devices" in args:
		devices.load()
	if "DeviceProblems" in args:
		device_problems.load()
	if "DeviceProblemCodes" in args:
		device_problem_codes.load()
	if "Patients" in args:
		patients.load()
