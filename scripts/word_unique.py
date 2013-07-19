import sys

filename = sys.argv[1]
new_filename = filename[0:filename.rfind('.')] + "_unique.txt"

words = set()
with open(filename, 'r') as f:
	for line in f.readlines():
		for word in line.split():
			words.add(word.lower())

with open(new_filename, 'w') as f:
	for word in sorted(words):
		f.write(word + "\n")
