from django.db import models
from nltk.corpus import wordnet
from nltk.stem import LancasterStemmer
lancaster = LancasterStemmer()


class Word(models.Model):
    root = models.CharField(max_length=20, default='')
    symbol = models.ImageField(upload_to='images/', default='')

    derivation1_symbol = models.ImageField(upload_to='images/', default='')
    derivation1_meaning1 = models.CharField(max_length=20, default='')
    derivation1_meaning2 = models.CharField(max_length=20, default='')
    derivation1_meaning3 = models.CharField(max_length=20, default='')
    derivation1_meaning4 = models.CharField(max_length=20, default='')
    derivation1_meaning5 = models.CharField(max_length=20, default='')


    derivation2_symbol = models.ImageField(upload_to='images/', default='')
    derivation2_meaning1 = models.CharField(max_length=20, default='')
    derivation2_meaning2 = models.CharField(max_length=20, default='')
    derivation2_meaning3 = models.CharField(max_length=20, default='')
    derivation2_meaning4 = models.CharField(max_length=20, default='')
    derivation2_meaning5 = models.CharField(max_length=20, default='')


    derivation3_symbol = models.ImageField(upload_to='images/', default='')
    derivation3_meaning1 = models.CharField(max_length=20, default='')
    derivation3_meaning2 = models.CharField(max_length=20, default='')
    derivation3_meaning3 = models.CharField(max_length=20, default='')
    derivation3_meaning4 = models.CharField(max_length=20, default='')
    derivation3_meaning5 = models.CharField(max_length=20, default='')


    derivation4_symbol = models.ImageField(upload_to='images/', default='')
    derivation4_meaning1 = models.CharField(max_length=20, default='')
    derivation4_meaning2 = models.CharField(max_length=20, default='')
    derivation4_meaning3 = models.CharField(max_length=20, default='')
    derivation4_meaning4 = models.CharField(max_length=20, default='')
    derivation4_meaning5 = models.CharField(max_length=20, default='')


    derivation5_symbol = models.ImageField(upload_to='images/', default='')
    derivation5_meaning1 = models.CharField(max_length=20, default='')
    derivation5_meaning2 = models.CharField(max_length=20, default='')
    derivation5_meaning3 = models.CharField(max_length=20, default='')
    derivation5_meaning4 = models.CharField(max_length=20, default='')
    derivation5_meaning5 = models.CharField(max_length=20, default='')


    derivation6_symbol = models.ImageField(upload_to='images/', default='')
    derivation6_meaning1 = models.CharField(max_length=20, default='')
    derivation6_meaning2 = models.CharField(max_length=20, default='')
    derivation6_meaning3 = models.CharField(max_length=20, default='')
    derivation6_meaning4 = models.CharField(max_length=20, default='')
    derivation6_meaning5 = models.CharField(max_length=20, default='')

