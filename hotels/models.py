from django.db import models


# Create your models here.
class Hotel(models.Model):
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
