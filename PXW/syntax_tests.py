import nltk
from nltk.corpus import wordnet


words = ["hello", "mouse", "aid"]

dictionary = {}


for word in words:
	synonyms = []
	for syn in wordnet.synsets(word):

		for l in syn.lemmas():
			synonyms.append(l.name())
	dictionary[word] = set(synonyms)

print(dictionary)

