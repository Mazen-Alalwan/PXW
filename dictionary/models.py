from django.db import models


class Word(models.Model):
    symbol = models.ImageField(upload_to='images/')
    main = models.CharField(max_length=20)

