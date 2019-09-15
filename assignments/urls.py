from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
    url(r'^$', views.assignments, name='assignments'),
    url(r'^addnewassignments/$', views.addnewassignments, name='addnewassignments'),
    # url(r'^deleteassignments/$', views.deleteassignments, name='deleteassignments'),
    url(r'^editassignments/$', views.editassignments, name='editassignments'),
    path('da/', views.deleteassignments, name='da'),
    path('allsubmissions/<assid>/', views.allsubmissions, name='allsubmissions'),
    path('evaluate/<submissionid>/', views.evaluate, name='evaluate'),
    path('submitgrade/<submissionid>/', views.submitgrade, name='submitgrade'),
    path('signout/', views.signout, name='signout'),
]