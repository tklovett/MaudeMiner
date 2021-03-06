#######################
# MaudeMiner Settings #
#######################

# Database settings
DATABASE_PATH = '/Users/tklovett/maude/'
DATABASE_NAME = 'maude'

# These setting control where the text files and zip files retrieved from the FDA website are stored
DATA_PATH = '/Users/tklovett/maude/data/'
ZIPS_PATH = DATA_PATH + 'zips/'
TXTS_PATH = DATA_PATH + 'txts/'

# The downloader module will use
MAUDE_DATA_ORIGIN = 'http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/PostmarketRequirements/ReportingAdverseEvents/ucm127891.htm'

LINES_PER_DB_COMMIT = 1000 * 50

# MaudeMiner will load any modules listed here
INSTALLED_MODULES = (
	"querier",
	"tokenizer",
	"html_generator",
	"cleanser",
)
