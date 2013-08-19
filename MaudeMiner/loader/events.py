from MaudeMiner.database import db
from MaudeMiner.maude.models import Event, Contact
from MaudeMiner.utils import update_progress
from MaudeMiner.loader.utils import *
from MaudeMiner.settings import LINES_PER_DB_COMMIT


EXPECTED_NUMBER_OF_FIELDS = 75


def load():
	# ensure tables exists
	db.create_tables(["Events", "Contacts"])

	print " === Loading Events === "

	files = get_files_with_prefix("mdrfoi", excludes=['mdrfoiChange', 'mdrfoiAdd'])

	for line in files:
		v = split_fields(line)
		if len(v) != EXPECTED_NUMBER_OF_FIELDS:
			continue

		# create distributor
		distributor = Contact()
		distributor.name         = v[16]
		distributor.street_1     = v[17]
		distributor.street_2     = v[18]
		distributor.city         = v[19]
		distributor.state_code   = v[20]
		distributor.zip_code     = v[21]
		distributor.zip_code_ext = v[22]
		db.save(distributor, commit=False)

		# create manufacturer
		manufacturer = Contact()
		manufacturer.name         = v[31]
		manufacturer.street_1     = v[32]
		manufacturer.street_2     = v[33]
		manufacturer.city         = v[34]
		manufacturer.state_code   = v[35]
		manufacturer.zip_code     = v[36]
		manufacturer.zip_code_ext = v[37]
		manufacturer.country_code = v[38]
		manufacturer.postal_code  = v[39]
		db.save(manufacturer, commit=False)

		# create manufacturer contact
		manufacturer_contact = Contact()
		manufacturer_contact.title_name            = v[40]
		manufacturer_contact.name                  = v[41] + " " + v[42]
		manufacturer_contact.street_1              = v[43]
		manufacturer_contact.street_2              = v[44]
		manufacturer_contact.city                  = v[45]
		manufacturer_contact.state_code            = v[46]
		manufacturer_contact.zip_code              = v[47]
		manufacturer_contact.zip_code_ext          = v[48]
		manufacturer_contact.country_code          = v[49]
		manufacturer_contact.postal_code           = v[50]
		manufacturer_contact.phone_no_area_code    = v[51]
		manufacturer_contact.phone_no_exchange     = v[52]
		manufacturer_contact.phone_no              = v[53]
		manufacturer_contact.phone_no_ext          = v[54]
		manufacturer_contact.phone_no_country_code = v[55]
		manufacturer_contact.phone_no_city_code    = v[56]
		manufacturer_contact.phone_no_local        = v[57]
		db.save(manufacturer_contact, commit=False)

		# create manufacturer g1
		manufacturer_g1 = Contact()
		manufacturer_g1.name         = v[58]
		manufacturer_g1.street_1     = v[59]
		manufacturer_g1.street_2     = v[60]
		manufacturer_g1.city         = v[61]
		manufacturer_g1.state_code   = v[62]
		manufacturer_g1.zip_code     = v[63]
		manufacturer_g1.zip_code_ext = v[64]
		manufacturer_g1.country_code = v[65]
		manufacturer_g1.postal_code  = v[66]
		db.save(manufacturer_g1, commit=False)

		# generate contact IDs
		db.flush()

		event = Event()
		event.report_key               = v[0]
		event.event_key                = v[1]
		event.report_number            = v[2]
		event.report_source_code       = v[3]
		event.manufacturer_link_flag   = v[4]
		event.number_devices_in_event  = v[5]
		event.number_patients_in_event = v[6]
		event.date_received            = v[7]

		# Section B
		event.adverse_event_flag       = v[8]
		event.product_problem_flag     = v[9]
		event.date_report              = v[10]
		event.date_of_event            = v[11]
		event.single_use_flag          = v[12]
		event.reporter_occupation_code = v[13]

		# Section E
		event.health_professional   = v[14]
		event.initial_report_to_fda = v[15]

		# Section F
		event.distributor_id              = distributor.id
		event.date_facility_aware         = v[23]
		event.type_of_report              = v[24]
		event.report_date                 = v[25]
		event.report_to_fda               = v[26]
		event.date_report_to_fda          = v[27]
		event.event_location              = v[28]
		event.report_to_manufacturer      = v[29]
		event.date_report_to_manufacturer = v[30]
		event.manufacturer_id             = manufacturer.id

		# Section G
		event.manufacturer_contact_id    = manufacturer_contact.id
		event.manufacturer_g1_id         = manufacturer_g1.id
		event.source_type                = v[67]
		event.date_manufacturer_received = v[68]

		# Section H
		event.device_date_of_manufacture = v[69]
		event.single_use_flag            = v[70]
		event.remedial_action            = v[71]
		event.previous_use_code          = v[72]
		event.removal_correction_number  = v[73]
		event.event_type                 = v[74]
		db.save(event, commit=False)


		if files.filelineno() % 1000 == 0:
			if files.filelineno() % LINES_PER_DB_COMMIT == 0:
				db.commit()
				update_progress("Loaded: ", files.filelineno(), LINES_IN_CURRENT_FILE[0])

	db.commit()
	print "\n # Done # \n"