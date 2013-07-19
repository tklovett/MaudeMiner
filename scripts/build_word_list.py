from nltk.corpus import wordnet

import nltk
from nltk.corpus import wordnet

def strip_non_ascii(s):
	return "".join(i for i in s if ord(i) < 128)

tokens = []
with open("C:/maude/data/tokens.txt", 'r') as f:
	for line in f:
		tokens.append(strip_non_ascii(line).strip().lower())

words = [x for x in tokens if wordnet.synsets(x)]
# for token in tokens:
# 	if wordnet.synsets(token): # filter out non-english words
# 		words.append(token)

# unique and sort
words = list(set(words))
words.sort()

with open("C:/maude/data/words.txt", 'w') as f:
	for word in words:
		f.write(word + "\n")
