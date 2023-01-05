from django.db import models

# Create your models here.
class Address(models.Model):
    street = models.CharField(max_length=255)
    number = models.IntegerField()
    city = models.CharField(max_length=255)
