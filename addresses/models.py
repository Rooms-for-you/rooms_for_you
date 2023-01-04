from django.db import models

class Address(models.Model):
    street = models.CharField(max_length=255)
    number = models.IntegerField(max_length=10)
    cep = models.IntegerField(max_length=10)