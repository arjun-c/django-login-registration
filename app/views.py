from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
from .models import User


def index(request):
    return render(request, 'registration.html')


def register(request):
    name = request.POST['name']
    username = request.POST['username']
    password = request.POST['password']
    user = User.objects.create(
        name=name,
        username=username,
        password=password,
    )
    return render(request, 'success.html')


def logpage(request):
    return render(request, 'login.html', { 'message':''})


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    try:
        user = User.objects.get(username=username, password=password)
        return render(request, 'logged.html', {'message': user.name})
    except User.DoesNotExist:
        return redirect('/loginpage', message="no user")