from django.db import models
from django.contrib.postgres.fields import JSONField
import nltk
from nltk.corpus import wordnet


derivation_num = 0
derivation_meaning_num = 0


class Root(models.Model):
    root = models.CharField(max_length=20, default='')
    root_symbol = models.ImageField(upload_to='images/', default='')

    def __str__(self):
        return self.root

    for a in range(5):
        derivation_meaning_num = 0
        derivation_num += 1
        exec('derivation' + str(derivation_num) + "_symbol" +
             " = models.ImageField(upload_to='images/', default='', blank=True)")
        for b in range(5):
            derivation_meaning_num += 1
            exec("derivation" + str(derivation_num) + "_meaning" + str(derivation_meaning_num) +
                 " = models.CharField(max_length=20, default='', blank=True)")


class Test(models.Model):
    test_name = models.CharField(max_length=20, default='')
    test_list = JSONField()

