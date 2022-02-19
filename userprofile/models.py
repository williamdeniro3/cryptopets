from django.db import models
from django.forms import CharField

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
