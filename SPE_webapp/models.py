from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # add additional fields here
    age = models.PositiveIntegerField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    is_admin=models.BooleanField(default=False)


class Jobs(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField()
    link = models.URLField()


class Post(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(null=True, blank=True, default=True)
    image = models.ImageField(upload_to='images/') 
    user =  models.ForeignKey(CustomUser, on_delete=models.CASCADE) 


class Comments(models.Model):
    text = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, default=True),






    
    