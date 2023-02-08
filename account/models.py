from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # add additional fields here
    age = models.PositiveIntegerField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='images/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    is_admin=models.BooleanField(default=False)

# Create your models here.
