from django.db import models

class Room(models.Model):
    number = models.IntegerField()
    beds = models.IntegerField()
    ranking = models.CharField(max_length=255)
    hotel = models.ForeignKey("hotels.Hotel", on_delete=models.CASCADE, related_name="rooms", null=True)

    services = models.ManyToManyField(
        "services.Service",
        related_name="Rooms",
        default=None
    )

    room_reservations = models.ManyToManyField("users.User", through="users.Reservations_users_rooms", related_name="user_reservations")
