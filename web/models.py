from django.db import models
from userhandling.models import Users

# Create your models here.

class Courses(models.Model):
    courseCode = models.CharField(max_length=20)
    courseTitle = models.CharField(max_length=50)
    instructor = models.ForeignKey(Users, on_delete=models.CASCADE)
    semester = models.CharField(max_length=50)
    enrollmentKey = models.CharField(max_length=50, unique=True, primary_key=True)

class Announcement(models.Model):
    teacher = models.ForeignKey(Users, on_delete=models.CASCADE)
    date = models.DateTimeField(null=True)
    announcement = models.CharField(max_length=300)
