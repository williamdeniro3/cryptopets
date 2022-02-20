from django.db import models
from django.forms import CharField

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)

class Pet(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=200)

