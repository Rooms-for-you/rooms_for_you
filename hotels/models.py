from django.db import models


# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="hotels",
    )
    address = models.OneToOneField(
        "addresses.Address",
        on_delete=models.CASCADE,
        related_name="hotel",
    )
