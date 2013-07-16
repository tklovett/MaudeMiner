from MaudeMiner import interactive
from MaudeMiner.querier import keyword_search
from MaudeMiner.querier import sql

def run(args):
	interactive.start("querier", 1, commands)

commands = {
	"keywords": keyword_search.run,
	"sql": sql.run,
}