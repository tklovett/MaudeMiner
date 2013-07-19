import nltk

def strip_non_ascii(s):
	return "".join(i for i in s if ord(i) < 128)

lines = []
with open("foitext.txt", 'r') as f:
	for line in f:
		lines.append(strip_non_ascii(line))

narratives = [x[x.rfind('|')+1:].strip() for x in lines]
tokens_list = [nltk.wordpunct_tokenize(x) for x in narratives]
# pos_list = [nltk.pos_tag(x) for x in tokens_list]

tokens = []
for x in tokens_list:
	for y in x:
		tokens.append(y)

tokens = list(set(tokens))
tokens.sort()

stem_functions = {
	"snwbl_eng": nltk.stem.snowball.EnglishStemmer().stem,
	"snwbl_snwbl": nltk.stem.snowball.SnowballStemmer("english").stem,
	"snwbl_prtr": nltk.stem.snowball.PorterStemmer().stem,
	"prtr": nltk.stem.porter.PorterStemmer().stem,
	"wordnet": nltk.stem.wordnet.WordNetLemmatizer().lemmatize,
	"lancaster": nltk.stem.lancaster.LancasterStemmer().stem
}

stems = {}


# Make stems
for name, func in stem_functions.items():
	this_stem = [func(x) for x in tokens]
	this_stem = list(set(this_stem))
	this_stem.sort()
	stems[name] = this_stem


# Print results
result = "Results:\n"
for name, stem_list in stems.items():
	result += name + ":\t" + str(len(stem_list)) + "\n"


print result
