from django.db import models
from web.models import Courses
from userhandling.models import Users
# Create your models here.
class Assignments(models.Model):
    course=models.ForeignKey(Courses,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    details=models.CharField(max_length=300)
    deadline=models.DateTimeField( null=True)
    totalmarks=models.IntegerField(null=True)

    def __str__(self):
        return self.title


class Submissions(models.Model):
    assignmentid = models.ForeignKey(Assignments, on_delete=models.CASCADE)
    studentid = models.CharField(max_length=50)
    ans = models.CharField(max_length=400)
    submissiondate = models.DateTimeField()
    givenmarks = models.FloatField(null=True)
    feedback = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.studentid