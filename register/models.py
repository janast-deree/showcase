from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True, default=None)

    REQUIRED_FIELDS = ['user', 'email']

    def __str__(self):
        return self.user.__str__()

