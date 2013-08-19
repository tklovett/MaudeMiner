# Define package settings here

DATABASE_PATH = 'C:/maude/'
DATABASE_NAME = 'maude'

DATA_PATH = 'C:/maude/data/'
ZIPS_PATH = DATA_PATH + 'zips/'
TXTS_PATH = DATA_PATH + 'txts/'

MAUDE_DATA_ORIGIN = 'http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/PostmarketRequirements/ReportingAdverseEvents/ucm127891.htm'

LINES_PER_DB_COMMIT = 1000 * 50

# These are the apps that MaudeMiner will recognize
# 'database' and 'maude' are built-ins and don't need to be included here
INSTALLED_MODULES = (
	"downloader",
	"loader",
	"querier",
	"tokenizer",
	"html_generator",
	"cleanser",
)