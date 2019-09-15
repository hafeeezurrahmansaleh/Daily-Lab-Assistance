from datetime import date

from django.shortcuts import render, redirect,   HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Announcement
from userhandling.models import Users
from attendance.models import Attendance

# Create your views here.
@login_required



def chat(request):
    return render(request, 'web/chat.html')

def insertAnnouncement(request):
    today = date.today()
    teachersID = request.session['user']
    teachers = Users.objects.get(pk=teachersID)
    announcement = request.GET['announcement']
    announcements = Announcement(announcement = announcement,teacher = teachers, date = today)
    announcements.save()

    return redirect('/web/viewannouncement')


def viewAnnouncement(request):
    uid = 10
    teachers = Users.objects.filter(pk = uid)
    announcements = Announcement.objects.filter(teacher__id = uid)
    context = {
        'announcements' : announcements,
        'instructor': teachers
    }
    return render(request,'web/home.html',context)

def getAttendance(request):
    attendance = Attendance.objects.all().values('date', 'studentid__id')
    context = {
        'attendance': attendance
    }
    return render(request, 'web/attendance.html', context)


def deleteannouncement(request,anid):
    announcements = Announcement.objects.get(pk=anid)
    announcements.delete()
    return redirect('/web/viewannouncement')



