from datetime import date
import io
from django.shortcuts import render, redirect,   HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Announcement, Courses
from userhandling.models import Users
from attendance.models import Attendance
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string

# from weasyprint import HTML
#
# def some_view(request):
#     announcements = Announcement.objects.filter(teacher__id=1)
#     html_string = render_to_string('web/home.html', {'announcement': announcements})
#
#     html = HTML(string=html_string)
#     html.write_pdf(target='/tmp/mypdf.pdf');
#
#     fs = FileSystemStorage('/tmp')
#     with fs.open('mypdf.pdf') as pdf:
#         response = HttpResponse(pdf, content_type='application/pdf')
#         response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
#         return response
#
#     return response
# from django.http import FileResponse
# from reportlab.pdfgen import canvas
# # @login_required
# def some_view(request):cabal install gtk2hs-buildtools
#     # Create a file-like buffer to receive PDF data.
#     buffer = io.BytesIO()
#
#     # Create the PDF object, using the buffer as its "file."
#     p = canvas.Canvas(buffer)
#
#     # Draw things on the PDF. Here's where the PDF generation happens.
#     # See the ReportLab documentation for the full list of functionality.
#     p.drawString(100, 100, "web/chat.html")
#
#     # Close the PDF object cleanly, and we're done.
#     p.showPage()
#     p.save()
#
#     # FileResponse sets the Content-Disposition header so that browsers
#     # present the option to save the file.
#     buffer.seek(0)
#     return FileResponse(buffer, as_attachment=True, filename='hello.pdf')


def chat(request):
    return render(request, 'web/chat.html')
def chat1(request):
    return render(request, 'web/chat1.html')

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
    teacher = Users.objects.get(pk = uid)
    announcements = Announcement.objects.filter(teacher__id = uid)
    course = Courses.objects.get(instructor = teacher)
    context = {
        'announcements' : announcements,
        'instructor': teacher,
        'course': course
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



