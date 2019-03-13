from .models import Word
from django.test import TestCase
import nltk
from nltk.corpus import wordnet

words = Word.objects.all()

print(words)
