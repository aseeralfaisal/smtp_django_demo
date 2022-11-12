from django.db import models

class Snippet(models.Model):
    title = models.CharField(max_length=200)
