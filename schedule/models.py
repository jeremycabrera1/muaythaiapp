from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class MuayClass1(models.Model):
    title = models.CharField(max_length=200, default='Untitled')
    coach = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.title
    
class Registration(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField(region='US',null=False, blank=False, unique=True)