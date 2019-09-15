from django.db import models
from web.models import Courses
from userhandling.models import Users
# Create your models here.
class Attendance(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    studentid = models.ForeignKey(Users, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)