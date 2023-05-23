from django.db import models

class Match(models.Model):
    text = models.TextField()
    regex_querry = models.CharField(max_length=300)
