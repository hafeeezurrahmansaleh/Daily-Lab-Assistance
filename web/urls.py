from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^chat/$', views.chat, name='chat'),
    # path('deleteassignment/', views.deleteassignment, name='deleteassignment' ),
    path('insertAnnouncement/',views.insertAnnouncement, name='insertAnnouncement'),
    path('viewannouncement/', views.viewAnnouncement, name='viewannouncement'),
    path('getattendance/', views.getAttendance, name='getattendance'),
    path('deleteannouncement/<anid>', views.deleteannouncement, name='deleteannouncement'),
]