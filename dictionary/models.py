from django.db import models

class Word(models.Model):
    id_word    = models.IntegerField()
    term       = models.CharField(max_length=30)
    definition = models.CharField(max_length=50)
    language   = models.CharField(max_length=5)
    category   = models.CharField(max_length=30)
    
"""
####BD Idea

Word
    id_word
    term
    definition
    language
    category

####Sample

Word

  | id | id_word | term    | definition | language | category |
  | -- | ------- | ----    | ---------- | -------- | -------- |
  | 01 | 01      | carro   | ...        | pt_br    | ...      | 
  | 02 | 01      | carrito | ...        | es_es    | ...      |

"""
