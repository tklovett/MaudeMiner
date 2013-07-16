from MaudeMiner.querier import keyword_search

def run(args):
	if "keyword" in args:
		keyword_search.run()
