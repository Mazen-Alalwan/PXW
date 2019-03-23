from django.db import models
from nltk.corpus import wordnet
from nltk.stem import LancasterStemmer
lancaster = LancasterStemmer()


class Word(models.Model):
    symbol = models.ImageField(upload_to='images/')
    main = models.CharField(max_length=20)

    def synonyms(self):
        synonyms = []
        for syn in wordnet.synsets(self.main):

            for l in syn.lemmas():
                synonyms.append(l.name())
        synonyms = sorted(set(synonyms[0:3]))
        return synonyms