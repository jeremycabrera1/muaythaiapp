from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.


class Reviews(models.Model):
    RATING = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    name = models.CharField(max_length=100, default="")
    rating = models.PositiveSmallIntegerField(
        default=1, choices=RATING, validators=[MaxValueValidator(5)])
    review = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.rating}/5'