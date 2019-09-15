from datetime import date

from django.shortcuts import render,redirect
from .models import Post, Comments
from userhandling.models import Users
# Create your views here.
def index(request):
    post = Post.objects.all().values('author__name','date','post','id')
    context = {
        'post' : post
     }
    return render(request,'post.html',context)

def addPost(request):
    userid = request.session['user']
    user = Users.objects.get(pk=userid)
    today = date.today()
    post = request.GET['textpost']
    addpost = Post(author = user, date = today, post = post)
    addpost.save()
    return redirect('/post')

def viewComment(request,postid):
    postAuthor = Post.objects.filter(pk = postid).values('author__name')
    post = Post.objects.get(pk = postid)
    comment = Comments.objects.filter(post=post)
    context = {
        'comment' : comment,
        'post' : post,
        'postauthor': postAuthor
    }
    return  render(request,'comment.html',context)


def addComment(request,postid):
    userid = request.session['user']
    user = Users.objects.get(pk = userid)
    post = Post.objects.get(pk =postid)
    comment = request.GET['txtcomment']
    addcomment = Comments(user = user , post = post , comment = comment )
    addcomment.save()
    return redirect('/post/viewcomment/'+ postid)

