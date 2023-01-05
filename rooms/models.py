from django.db import models

class Room(models.Model):
    number = models.IntegerField()
    beds = models.IntegerField()
    ranking = models.CharField(max_length=255)
    
    services = models.ManyToManyField(
        "services.Service",
        related_name="Rooms",
        default=None
    )