from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from assignments.models import Assignments
from userhandling.models import Users
from web.models import Courses, Announcement
from attendance.models import Attendance
from assignments.models import Assignments, Submissions
from .models import CourseEnrolled
from datetime import date

# Create your views here.


def index(request):
    if 'user' not in request.session:
        return redirect('/userhandling/login')
    return render(request, 'spanel/home.html')


def enrollcourse(request):
    today = date.today()
    userid = request.session['user']
    global studentinfo
    studentinfo = Users.objects.get(pk=userid)
    message = ''
    if not Courses.objects.filter(enrollmentKey = request.POST['enrollkey']).exists():
        try:
            global courseinfo
            courseinfo = Courses.objects.get(enrollmentKey = request.POST['enrollkey'])
            enroll = CourseEnrolled(student = studentinfo, course = courseinfo)
            enroll.save()
            message = 'Successfully enrolled!!'
        except:
            message = 'Failed!!'
    courseinfo = Courses.objects.get(enrollmentKey=request.POST['enrollkey'])


    if not Attendance.objects.filter(course = courseinfo, studentid = studentinfo,
                                     date__year=today.year,
                                       date__month=today.month,
                                       date__day=today.day).exists():
        attend = Attendance(course=courseinfo, studentid = studentinfo)
        attend.save()
    context = {
        'student': studentinfo,
        'message': message
    }
    return render(request,'spanel/home.html', context)


def coursedetails(request,courseid):
    if 'user' not in request.session:
        return redirect('/userhandling/login')
    global studentinfo, userid, currentcourse
    currentcourse=courseid
    userid = request.session['user']
    studentinfo = Users.objects.get(pk=userid)
    courseinfo = Courses.objects.get(enrollmentKey = courseid)
    assignments = Assignments.objects.filter(course = courseinfo)

    announcements = Announcement.objects.filter(teacher__courses__enrollmentKey=courseid)
    numofclasses = Attendance.objects.filter(course=courseid).count()
    mayattendance = Attendance.objects.filter(course=courseid, studentid = studentinfo).count()
    assignedwork = Assignments.objects.filter(course=courseinfo).count()
    mysubmissions = Submissions.objects.filter(studentid = studentinfo.email, assignmentid__course=courseinfo, ).count()
    assignmentdue = assignedwork-mysubmissions
    context = {
        'assignment': assignments,
        'course':courseinfo,
        'numofclasses':numofclasses,
        'mayattendance':mayattendance,
        'assignedwork':assignedwork,
        'mysubmissions':mysubmissions,
        'assignmentdue':assignmentdue,
        'announcements': announcements
    }
    return render(request, 'coursedetails.html', context)

def archive(request):
    if 'user' not in request.session:
        return redirect('/userhandling/login')
    return render(request, 'archive.html')

def signout(request):
    try:
        del request.session['user']
    except:
        pass
    return redirect('/userhandling')

def submitAssignment(request,id):

    assignment = Assignments.objects.get(pk=id)
    userid = request.session['user']
    try:
        submission = Submissions.objects.get(assignmentid = assignment, studentid=userid)
    except:
        submission = assignment;
        submission = assignment;
    context = {
        'assignment' : assignment,
        'submission': submission
    }
    return render(request,'submit.html',context)

def submitAns(request,assid):
    today = date.today()
    studentid = request.session['user']
    assignment = Assignments.objects.get(pk=assid)
    ans = request.GET['ans']


    if Submissions.objects.filter(assignmentid = assignment, studentid=studentid).exists():
        updatesubmission = Submissions.objects.get(assignmentid = assignment, studentid=studentid)
        updatesubmission.ans = ans
        updatesubmission.save()
    else:
        submit=Submissions(assignmentid = assignment,studentid = studentid,ans = ans, submissiondate = today)
        submit.save()

    course = Courses.objects.get(assignments__pk=assid)
    return redirect('/studentpanel/coursedetails/'+course.enrollmentKey)

def deleteSubmission(request,submissionid):
    submission = Submissions.objects.get(pk=submissionid)
    submission.delete()
    return redirect('/studentpanel/coursedetails/' + currentcourse)