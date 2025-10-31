from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField


User = get_user_model()
# Create your models here.


class MuayClass(models.Model):
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
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registrations')
    muay_class = models.ManyToManyField('MuayClass', related_name='classes')
    def __str__(self):
        return f'{self.name} {self.last_name}'
    

class Reviews(models.Model):
    RATING = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    name = models.CharField(max_length=100, default="")
    rating = models.PositiveSmallIntegerField(default=1, choices=RATING, validators=[MaxValueValidator(5)])
    review = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.rating}/5'
