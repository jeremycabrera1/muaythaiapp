from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from django.db import models

# Create your models here.
User = get_user_model()


class Reviews(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="review", default="Unknown")
    RATING = (
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    )
    rating = models.PositiveSmallIntegerField(
        default=1, choices=RATING, validators=[MaxValueValidator(5)]
    )
    review = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.owner} - {self.rating}/5"
