from .models import Word
from django.test import TestCase
import nltk
from nltk.corpus import wordnet


def synonyms():
    synonyms = []
    for syn in wordnet.synsets("hello"):

        for l in syn.lemmas():
            synonyms.append(l.name())
    synonyms = sorted(set(synonyms[0:3]))
    return synonyms


for synonym in synonyms("hello"):
    print(synonym)