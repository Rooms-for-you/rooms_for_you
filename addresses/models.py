from django.db import models

class Address(models.Model):
    street = models.CharField(max_length=255)
    number = models.IntegerField()
    city = models.CharField(max_length=255)
    cep = models.CharField(max_length=9)