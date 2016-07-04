from django.db import models

class Word(models.Model):
    term = models.CharField(max_length=30)
    meaning = model.CharField(max_length=100)
