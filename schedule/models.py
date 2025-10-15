from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
User = get_user_model()

class MuayClass1(models.Model):
    title = models.CharField(max_length=100, default='Untitled')
    coach = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.title


class Registration(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField(region='US', null=False, blank=False, unique=True)

    def __str__(self):
        return f'{self.name} {self.last_name}'
    

class Reviews(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField(default=1, validators=[MaxValueValidator(5)])
    review = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.owner.username} - {self.rating}/5'
