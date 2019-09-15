from .import views
from django.urls import path

urlpatterns = [
    path('',views.index, name='index'),
    path('/addpost',views.addPost, name='addpost'),
    path('/viewcomment/<postid>',views.viewComment, name='viewcomment'),
    path('/addcomment/<postid>',views.addComment, name='addcomment'),
]