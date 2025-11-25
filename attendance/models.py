from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Registration(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='registrations'
    )
    muay_class = models.ManyToManyField(
        'classes.MuayClass', related_name='registrations'
    )

    def __str__(self):
        return f'{self.owner.username}'
