from django.db import models

# Create your models here.
class Navbat(models.Model):
    name = models.CharField(max_length=50)