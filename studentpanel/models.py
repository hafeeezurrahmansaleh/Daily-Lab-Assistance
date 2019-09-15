from django.db import models
from userhandling.models import Users
from web.models import Courses
# Create your models here.

class CourseEnrolled(models.Model):
    student = models.ForeignKey(Users, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)