import nltk
from nltk.corpus import wordnet

words = []
with open("C:/maude/data/words.txt", 'r') as f:
	for line in f:
		words.append(line.strip())

print "Stemming..."

# Make stems
stems = [nltk.stem.snowball.EnglishStemmer().stem(x) for x in words]
stems = list(set(stems))
stems.sort()

with open("C:/maude/data/stems.txt", 'w') as f:
	for stem in stems:
		f.write(stem + "\n")