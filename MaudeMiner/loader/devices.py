from MaudeMiner.database import db
from MaudeMiner.maude.models import Device
from MaudeMiner.utils import update_progress
from MaudeMiner.loader.utils import *
from MaudeMiner.settings import LINES_PER_DB_COMMIT


EXPECTED_NUMBER_OF_FIELDS = 45


def load():
	# ensure tables exists
	db.create_tables(["Devices"])

	print " === Loading Devices === "

	files = get_files_with_prefix("foidev", excludes=['foidevproblem', 'foidevAdd', 'foidevChange'])

	for line in files:
		v = split_fields(line)
		if len(v) != EXPECTED_NUMBER_OF_FIELDS:
			continue

		device = Device()
		device.report_key                             = v[0]
		device.device_event_key                       = v[1]
		device.implant_flag                           = v[2]
		device.date_removed_flag                      = v[3]
		device.device_sequence_number                 = v[4]
		device.date_received                          = v[5]
		device.brand_name                             = v[6]
		device.generic_name                           = v[7]
		device.manufacturer_name                      = v[8]
		device.manufacturer_address_1                 = v[9]
		device.manufacturer_address_2                 = v[10]
		device.manufacturer_city                      = v[11]
		device.manufacturer_state_code                = v[12]
		device.manufacturer_zip_code                  = v[13]
		device.manufacturer_zip_code_ext              = v[14]
		device.manufacturer_country_code              = v[15]
		device.manufacturer_postal_code               = v[16]
		device.expiration_date_of_device              = v[17]
		device.model_number                           = v[18]
		device.lot_number                             = v[19]
		device.catalog_number                         = v[20]
		device.other_id_number                        = v[21]
		device.device_operator                        = v[22]
		device.device_availability                    = v[23]
		device.date_reported_to_manufacturer          = v[24]
		device.device_report_product_code             = v[25]
		device.device_age                             = v[26]
		device.device_evaluated_by_manufacturer       = v[27]
		device.baseline_brand_name                    = v[28]
		device.baseline_generic_name                  = v[29]
		device.baseline_model_number                  = v[30]
		device.baseline_catalog_number                = v[31]
		device.baseline_other_id_number               = v[32]
		device.baseline_device_family                 = v[33]
		device.baseline_shelf_life_contained_in_label = v[34]
		device.baseline_shelf_life_in_months          = v[35]
		device.baseline_pma_flag                      = v[36]
		device.baseline_pma_number                    = v[37]
		device.baseline_510k_flag                     = v[38]
		device.baseline_510k_number                   = v[39]
		device.baseline_preamendment                  = v[40]
		device.baseline_transitional                  = v[41]
		device.baseline_510k_exempt_flag              = v[42]
		device.baseline_date_first_marketed           = v[43]
		device.baseline_date_ceased_marketing         = v[44]
		db.save(device, commit=False)


		if files.lineno() % 1000 == 0:
			update_progress("Loaded: ", files.lineno(), LINES_IN_CURRENT_FILE[0])
			if files.lineno() % LINES_PER_DB_COMMIT == 0:
				db.commit()

	db.commit()
	print "\n # Done # \n"