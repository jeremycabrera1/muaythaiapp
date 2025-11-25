from django.db import models

# Create your models here.


class MuayClass(models.Model):
    title = models.CharField(max_length=100, default='Untitled')
    coach = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.title
