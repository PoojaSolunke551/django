from django.db import models

# Create your models here.

class User(models.Model):
    user=models.CharField(max_length = 255)

class BlogPost(models.Model):
    auther=models.ForeignKey(User,on_delete = models.CASCADE)
    title=models.TextField()
    body=models.TextField()
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField()



