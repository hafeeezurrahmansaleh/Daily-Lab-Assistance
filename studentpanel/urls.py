from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('coursedetails/<courseid>', views.coursedetails, name='coursedetails'),
    path('archive/', views.archive, name='archive'),
    path('enrollcourse/', views.enrollcourse, name='enrollcourse'),
    path('submitassignment/<id>', views.submitAssignment, name='submitassignment'),
    path('submitans/<assid>', views.submitAns, name='submitans'),
    path('deletesubmission/<submissionid>/', views.deleteSubmission, name='deletesubmission'),
    path('signout/', views.signout, name='signout'),

    # path('', views.index, name='index'),
]