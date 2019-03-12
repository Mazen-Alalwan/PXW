from django.shortcuts import render
import nltk
from nltk.corpus import wordnet
from .models import Word


def home(request):
    words = Word.objects

    dictionary = {}

    for word in words.all():
        synonyms = []
        for syn in wordnet.synsets(word.main):

            for l in syn.lemmas():
                synonyms.append(l.name())
        dictionary[word.main] = set(synonyms)

    return render(request, "dictionary/home.html", {'words': words, 'dictionary': dictionary.items()})

