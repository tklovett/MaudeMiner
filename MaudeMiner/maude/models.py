from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from MaudeMiner.database.base import base


def create(engine, tables=[]):
	print " === Creating Table(s) === "
	for t in tables:
		print "  " + str(t)
	base.metadata.create_all(engine, tables=tables)
	print "Done."

def drop(engine, tables=[]):
	print " === Dropping Table(s) === "
	for t in tables:
		print "  " + str(t)
	base.metadata.drop_all(engine, tables=tables)
	print "Done."

class Event(base):
	"""
	Comes from mdrfoi*.txt
	"""
	__tablename__ = "Events"

	report_key = Column(Integer, primary_key=True)
	event_key = Column(Integer)
	report_number = Column(String)
	report_source_code = Column(String)
	manufacturer_link_flag = Column(String)
	number_devices_in_event = Column(Integer)
	number_patients_in_event = Column(Integer)
	date_received = Column(String)

	# Section B
	adverse_event_flag = Column(String)
	product_problem_flag = Column(String)
	date_report = Column(String)
	date_of_event = Column(String)
	single_use_flag = Column(String)
	reporter_occupation_code = Column(String)

	# Section E
	health_professional = Column(String)
	initial_report_to_fda = Column(String)

	# Section F
	distributor_id = Column(Integer, ForeignKey('Contacts.id'))
	date_facility_aware = Column(String)
	type_of_report = Column(String)
	report_date = Column(String)
	report_to_fda = Column(String)
	date_report_to_fda = Column(String)
	event_location = Column(String)
	report_to_manufacturer = Column(String)
	date_report_to_manufacturer = Column(String)
	manufacturer_id = Column(Integer, ForeignKey('Contacts.id'))

	# Section G
	manufacturer_contact_id = Column(Integer, ForeignKey('Contacts.id'))
	manufacturer_g1_id = Column(Integer, ForeignKey('Contacts.id'))
	source_type = Column(String)
	date_manufacturer_received = Column(String)

	# Section H
	device_date_of_manufacture = Column(String)
	single_use_flag = Column(String)
	remedial_action = Column(String)
	previous_use_code = Column(String)
	removal_correction_number = Column(Integer)
	event_type = Column(String)

class Contact(base):
	"""
	"""
	__tablename__ = "Contacts"

	nextId = 0

	id = Column(Integer, primary_key=True, autoincrement='ignore_fk')

	title_name = Column(String)
	name = Column(String)
	street_1 = Column(String)
	street_2 = Column(String)
	city = Column(String)
	state_code = Column(String)
	zip_code = Column(String)
	zip_code_ext = Column(String)
	country_code = Column(String)
	postal_code = Column(String)
	phone_no_area_code = Column(String)
	phone_no_exchange = Column(String)
	phone_no = Column(String)
	phone_no_ext = Column(String)
	phone_no_country_code = Column(String)
	phone_no_city_code = Column(String)
	phone_no_local = Column(String)

	def __repr__(self):
		return "<Contact(%s,%s,%s)>" %(self.id, self.name, self.street_1)


class DeviceProblemCode(base):
	"""
	Comes from deviceproblemcodes.txt
	"""
	__tablename__ = "DeviceProblemCodes"

	code = Column(Integer, primary_key=True, autoincrement=False)
	description = Column(String)

	def __init__(self, code=None, description=None):
		self.code = code
		self.description = description

	def __repr__(self):
		return "<DeviceProblemCode('%s','%s')>" %(self.code, self.description)

class Device(base):
	"""
	Comes from foidev*.txt (except foidevproblem.txt)
	"""
	__tablename__ = "Devices"

	id = Column(Integer, primary_key=True)

	report_key = Column(Integer, ForeignKey('Events.report_key'))
	device_event_key = Column(Integer)
	implant_flag = Column(String)
	date_removed_flag = Column(String)
	device_sequence_number = Column(String)
	date_received = Column(String)

	# Section D
	brand_name = Column(String)
	generic_name = Column(String)
	manufacturer_name = Column(String)
	manufacturer_address_1 = Column(String)
	manufacturer_address_2 = Column(String)
	manufacturer_city = Column(String)
	manufacturer_state_code = Column(String)
	manufacturer_zip_code = Column(String)
	manufacturer_zip_code_ext = Column(String)
	manufacturer_country_code = Column(String)
	manufacturer_postal_code = Column(String)
	expiration_date_of_device = Column(String)
	model_number = Column(String)
	lot_number = Column(String)
	catalog_number = Column(String)
	other_id_number = Column(String)
	device_operator = Column(String)
	device_availability = Column(String)
	date_reported_to_manufacturer = Column(String)
	device_report_product_code = Column(String)
	device_age = Column(String)
	device_evaluated_by_manufacturer = Column(String)

	# Baseline Section
	baseline_brand_name = Column(String)
	baseline_generic_name = Column(String)
	baseline_model_number = Column(String)
	baseline_catalog_number = Column(String)
	baseline_other_id_number = Column(String)
	baseline_device_family = Column(String)
	baseline_shelf_life_contained_in_label = Column(String)
	baseline_shelf_life_in_months = Column(String)
	baseline_pma_flag = Column(String)
	baseline_pma_number = Column(String)
	baseline_510k_flag = Column(String)
	baseline_510k_number = Column(String)
	baseline_preamendment = Column(String)
	baseline_transitional = Column(String)
	baseline_510k_exempt_flag = Column(String)
	baseline_date_first_marketed = Column(String)
	baseline_date_ceased_marketing = Column(String)


class DeviceProblem(base):
	"""
	Comes from foidevproblem.txt
	"""
	__tablename__ = "DeviceProblems"

	report_key = Column(Integer, ForeignKey('Events.report_key'), primary_key=True, autoincrement=False)
	code       = Column(Integer, ForeignKey('DeviceProblemCodes.code'), primary_key=True, autoincrement=False)

	def __repr__(self):
		return "<DeviceProblem('%s','%s')>" %(self.report_key, self.device_problem_code)

class Narrative(base):
	"""
	Comes from foitext*.txt
	"""
	__tablename__ = "Narratives"

	report_key = Column(Integer, ForeignKey('Events.report_key'))
	text_key = Column(Integer, primary_key=True, autoincrement='False')
	text_type_code = Column(String)
	patient_sequence_number = Column(String)
	date_report = Column(String)
	text = Column(String)

	event = relationship("Event")

	def __repr__(self):
		return "<Narrative('%s','%s')>" %(self.report_key, self.text[0:10])

class Patient(base):
	"""
	Comes from patient*.txt
	"""
	__tablename__ = "Patients"

	id = Column(Integer, primary_key=True, autoincrement='ignore_fk')

	report_key = Column(Integer, ForeignKey('Events.report_key'))
	patient_sequence_number = Column(String)
	date_received = Column(String)
	sequence_number_treatment = Column(String)
	sequence_number_outcome = Column(String)

	def __repr__(self):
		return "<Patient('%s','%s', '%s')>" %(self.report_key, self.patient_sequence_number, self.date_received)


# Map and register models with the database
model_map = {
	"Event": Event,
	"DeviceProblemCode": DeviceProblemCode,
	"Device": Device,
	"DeviceProblem": DeviceProblem,
	"Narrative": Narrative,
	"Patient": Patient,
	"Contact": Contact,
}
# maude.database.registry.register_models(model_map)

table_map = {}
for m in model_map:
	table_map[m + "s"] = model_map[m]

# maude.database.registry.register_tables(table_map)
