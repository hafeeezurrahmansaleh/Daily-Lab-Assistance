from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    url(r'^chat/$', views.chat, name='chat'),
    # path('deleteassignment/', views.deleteassignment, name='deleteassignment' ),
    path('insertAnnouncement/',views.insertAnnouncement, name='insertAnnouncement'),
    path('viewannouncement/', views.viewAnnouncement, name='viewannouncement'),
    path('getattendance/', views.getAttendance, name='getattendance'),
    path('deleteannouncement/<anid>', views.deleteannouncement, name='deleteannouncement'),
    path('chat/', views.chat, name='chat'),
    path('chat1/', views.chat1, name='chat1'),
    # path('some_view/', views.some_view, name='some_view'),
    # path('studentprogress/', views.studentprogress, name='studentprogress'),
    # url(r'^studentprogress/', include('studentprogress.urls')),
]