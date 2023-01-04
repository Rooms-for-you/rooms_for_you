from django.db import models

class Room(models.Model):
    number = models.IntegerField(max_length=10)
    beds = models.IntegerField(max_length=1)
    ranking = models.CharField(max_length=255)
    
    services = models.ManyToManyField(
        "services.Service",
        related_name="Rooms",
        default=None
    )