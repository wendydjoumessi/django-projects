from django.db import models

# Create your models here.

class member(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    