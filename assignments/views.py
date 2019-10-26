from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Assignments, Submissions
from web.models import Courses, Users

# # To encrypt the password. This creates a password hash with a random salt.
# password_hash = crypt.crypt(password)
#
# # To check the password.
# valid_password = crypt.crypt(cleartext, password_hash) == password_hash

# Create your views here.

def assignments(request):
    if 'user' not in request.session:
       return redirect('/userhandling/')
    # assignments = Assignments.objects.all()
    # submissions = Submissions.objects.filter()
    else:
        global courses, user, course
        userid = request.session['user']
        user = Users.objects.get(pk = userid)
        courses = Courses.objects.get(instructor = user)
        course=courses.enrollmentKey
        totalstudent=7
        submissions= Assignments.objects.filter(course = courses).values('submissions__assignmentid','id','title','details','deadline','totalmarks').annotate(submitted=Count('submissions__assignmentid'),notsubmitted=totalstudent-Count('submissions__assignmentid'))
        context= {
        'assignments': submissions,
        'course':course,
        'user':user
        }
        return render(request, 'listofassignment.html', context)

def addnewassignments(request):
    print(request.POST)
    title = request.GET['title']
    details = request.GET['details']
    deadline = request.GET['deadline']
    totalmarks=request.GET['totalmarks']
    ass_details = Assignments(course=courses, title=title, details=details, deadline=deadline, totalmarks=totalmarks)
    ass_details.save()
    return redirect('/assignments')

def editassignments(request):
    id = request.GET['hiddenedit']
    assignment = Assignments.objects.get(pk=id)
    assignment.title = request.GET['etitle']
    assignment.details = request.GET['edetails']
    assignment.deadline = request.GET['edeadline']
    assignment.totalmarks=request.GET['etotalmarks']
    assignment.save()
    return redirect('/assignments')

def deleteassignments(request):

    id=request.POST['hiddenid']
    assignment = Assignments.objects.get(pk=id)
    assignment.delete()
    return redirect('/assignments')

def allsubmissions(request, assid):
    global assignmentid
    assignmentid=assid
    allsubmission = Submissions.objects.filter(assignmentid=assid)
    assignmenttitle = Assignments.objects.only('title').get(pk=assid).title
    context={
        'submissions':allsubmission,
        'asstitle':assignmenttitle,
        'course': course,
        'user': user
    }
    return render(request,'submissions.html',context)

def evaluate(request, submissionid):
    if 'user' not in request.session:
       return redirect('/userhandling/login')
    submission = Submissions.objects.get(pk=submissionid)
    assinfo= Assignments.objects.get(pk=assignmentid)
    context={
        'submission':submission,
        'assinfo':assinfo,
        'course': course,
        'user': user
    }
    return  render(request, 'evaluate.html', context)

def submitgrade(request, submissionid):
    submission  = Submissions.objects.get(pk=submissionid)
    submission.givenmarks = request.GET['givenmarks']
    submission.feedback = request.GET['feedback']
    submission.save()
    return redirect('/assignments/allsubmissions/'+str(assignmentid))

def signout(request):
    try:
        del request.session['user']
    except:
       pass
    return redirect('/userhandling/')