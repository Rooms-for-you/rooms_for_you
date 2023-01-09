from django.db import models


class Rating(models.IntegerChoices):
    PÉSSIMO = 0
    RUIM = 1
    REGULAR = 2
    BOM = 3
    MUITO_BOM = 4
    EXCELENTE = 5


class Feedback(models.Model):
    rating = models.CharField(
        max_length=12,
        choices=Rating.choices,
    )

    description = models.CharField(
        max_length=256,
        null=True,
    )

    hotel = models.ForeignKey(
        "hotels.Hotel",
        on_delete=models.CASCADE,
        related_name="feedbacks",
    )

    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="feedbacks",
    )
