from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ArticleModel(models.Model):
    title = models.CharField(max_length=155)
    body = models.TextField()
    image = models.ImageField(upload_to = 'images/')
    author = models.ForeignKey(User, on_delete=models.SET_NULL , null = True)
    author2 = User
    
    
    def __str__(self):
        return self.title
    