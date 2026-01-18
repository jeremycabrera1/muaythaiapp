from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

# Create your models here.


class Registration(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="registrations")
    muay_class = models.ForeignKey("classes.MuayClass", on_delete=models.CASCADE, related_name="registrations")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("owner", "muay_class")