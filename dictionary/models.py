from django.db import models

class Word(models.Model):
    id_word    = models.IntegerField()
    language   = models.ForeignKey(Language, on_delete=models.CASCADE)
    term       = models.CharField(max_length=30)
    definition = models.CharField(max_length=50)
    category   = models.CharField(max_length=30)

    def __str__(self):
        return "({0} - {1}) {2}: {3}".format(id_word, language, term, definition)

class Language(models.Model):
    language = models.CharField(max_length=5, primary_key=True)
    alphabet = models.CharField(max_length=50)

    def __str__(self):
        return "{0}: {1}".format(language, alphabet)
    
"""
####Sample

Word
  | id | id_word | language | id_word | term    | definition | category |
  | -- | ------- | -------- | ------- | ----    | ---------- | -------- |
  | 01 | 01      | pt_br    | 01      | olá     | ...        | ...      | 
  | 02 | 01      | es_es    | 01      | hello   | ...        | ...      |

Language

  | language |           alphabet          |
  | -------- | --------                    |
  | pt-br    | abcdefghijklmnopqrstuvwxyz  |
  | en-us    | abcdefghijklmnopqrstuvwxyz  |
  | es-es    | abcdefghijklmnñopqrstuvwxyz |
"""
