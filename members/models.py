from django.db import models
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

User = get_user_model()

class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(region='US', unique=True)

    def __str__(self):
        return f'{self.owner.username}'
