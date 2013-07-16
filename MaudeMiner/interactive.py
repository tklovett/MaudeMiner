def print_routes(routes):
	print "Usage: <command> <arg1> <arg2> ..."
	print "Available commands:"
	for route in routes.keys():
		print "\t" + route

def start(prompt, level, routes=None, process_input=None):
	full_prompt = "|" + "-"*level + " " + prompt + "> "
	
	while True:
		text = raw_input(full_prompt)

		if text == "":
			continue

		if text == "exit":
			return

		if text == "help":
			print_routes(routes)
			continue

		
		if routes == None:
			process_input(text)
			continue

		args = text.split()
		command = args[0]
		if command in routes:
			routes[command](args[1:])
		else:
			print "Command not recognized. Enter \"help\" for a list of commands"