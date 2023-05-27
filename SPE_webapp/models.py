from django.db import models
from account.models import CustomUser




class Jobs(models.Model):
    title = models.CharField(max_length=255,blank=True,null=True)
    content = models.TextField()
    link = models.URLField()



class Post(models.Model):
    title = models.CharField(max_length=255,blank=True,null=True)
    content = models.TextField(null=True,blank=True,default=True)
    image = models.ImageField(upload_to='images/') 
    users_liked = models.ManyToManyField(CustomUser, related_name='liked_posts', through='likes')
   

class Comments(models.Model):
    text = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,default=True),

class likes(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')






    
    