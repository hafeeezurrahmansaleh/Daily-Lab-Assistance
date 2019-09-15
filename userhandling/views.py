from django.shortcuts import render,redirect
from .models import Users
from web.models import Courses
from django.contrib.auth import login
# Create your views here.
def index(request,):
    if request.method == 'POST':
        instructor = Users(name=request.POST['name'],email=request.POST['email'], password=request.POST['password'], role='instructor')
        instructor.save()
        ins = Users.objects.get(email=request.POST['email'])
        course = Courses(courseCode=request.POST['coursecode'],courseTitle=request.POST['coursetitle'],instructor=ins,semester=request.POST['semester'],enrollmentKey=request.POST['coursecode']+request.POST['semester']+request.POST['initial'],)
        course.save()
        context = {'msg': 'Registration Successfull!!'}
        return redirect('/userhandling', context)
    else:
        context = {'msg': ''}
        return render(request, 'index.html', context)

def studentsignup(request):
    if request.method == 'POST':
        student = Users(name=request.POST['studentname'],email=request.POST['studentId'], password=request.POST['password'], role='student')
        student.save()
        context = {'msg': 'Registration Successfull!!'}
        return redirect('/userhandling/login', context)
    else:
        context = {'msg': ''}
        return render(request, 'studentsignup.html', context)
def login(request):
    return render(request, 'login1.html')

def home(request):
    try:
        if request.method == 'POST':
            if Users.objects.filter(email=request.POST['email'], password=request.POST['password'], role='instructor').exists():
                instructor = Users.objects.get(email=request.POST['email'], password=request.POST['password'])
                # request.session['instructor']=instructor.id
                login(request)
                request.session["user"] = instructor.id
                # return render(request, 'web/home.html', {'instructor': instructor})
                return redirect('/web/viewannouncement')
            elif Users.objects.filter(email=request.POST['email'], password=request.POST['password'], role='student').exists():
                student = Users.objects.get(email=request.POST['email'], password=request.POST['password'])
                # request.session['student'] = student.id
                login(request)
                request.session["user"] = student.id
                return render(request, 'spanel/home.html', {'student': student})

            else:
                context = {'msg': 'Invalid username or password'}
                return render(request, 'login1.html', context)
    except:
        context = {'msg': 'Invalid username or password'}
        return render(request, 'login1.html', context)