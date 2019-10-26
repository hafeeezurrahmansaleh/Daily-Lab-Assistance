from django.shortcuts import render, redirect,   HttpResponseRedirect


def dashboard(request):
    return render(request, 'chart.html')