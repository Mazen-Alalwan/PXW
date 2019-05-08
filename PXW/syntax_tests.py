import nltk
from nltk.corpus import wordnet






synonyms = []
for syn in wordnet.synsets("to improve"):

	for l in syn.lemmas():
		synonyms.append(l.name())
	synonyms = sorted(synonyms)


print(set(synonyms))

