from django.db import models
from userhandling.models import Users
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(Users,on_delete=models.CASCADE)
    date = models.DateTimeField()
    post = models.CharField(max_length=200)


class Comments(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)