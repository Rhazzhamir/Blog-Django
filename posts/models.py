from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    CategoryName = models.CharField(max_length=255)

    def __str__(self):
        return self.CategoryName

class Post(models.Model):
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    intro = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ('-created_at' , )
    
    def __str__(self):
        return self.title
    


    