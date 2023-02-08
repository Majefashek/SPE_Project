from django.db import models
from  account.models import CustomUser
from SPE_webapp.models import Post

class likes(models.Model):
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    



# Create your models here.
