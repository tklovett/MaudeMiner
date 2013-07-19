from nltk.corpus import wordnet

import nltk
from nltk.corpus import wordnet

def strip_non_ascii(s):
	return "".join(i for i in s if ord(i) < 128)

filename = raw_input("tokens filename: ")

lines = []
with open(filename, 'r') as f:
	for line in f:
		lines.append(strip_non_ascii(line))

narratives = [x[x.rfind('|')+1:].strip() for x in lines]
tokens_list = [nltk.wordpunct_tokenize(x) for x in narratives]
# pos_list = [nltk.pos_tag(x) for x in tokens_list]

print "Tokenizing..."

tokens = []
for row in tokens_list:
	for token in row:
		if wordnet.synsets(token): # filer out non-english words
			tokens.append(token)

tokens = list(set(tokens))
tokens.sort()

print "Stemming..."

# Make stems
stems = [nltk.stem.snowball.EnglishStemmer().stem(x) for x in tokens]
stems = list(set(stems))
stems.sort()

print "Writing..."

with open("stems.txt", 'w') as f:
	for stem in stems:
		f.write(stem + "\n")