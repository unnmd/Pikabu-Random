from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Pikabu(models.Model):
    ratio_post = models.BigIntegerField()
    date_post = models.DateField()
    href_post = models.TextField()
