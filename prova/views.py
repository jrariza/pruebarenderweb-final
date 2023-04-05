from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.http import HttpResponse
from .forms import RegisterForm

# Create your views here.

def hello_world(request):
    html = '<h1>HELLO<h1/>' + '<br/>' + '<h1>WORLD<h1/>' + '<br/>' +\
        '<a href="/login/">LOGIN</a>' + '<br/>' + '<a href="/sign_up/">SIGNUP</a>'
    return HttpResponse(html)

@login_required
def you_are_in(request):
    html = '<h1>YOU<h1/>' + '<br/>' + '<h1>ARE<h1/>' + '<br/>' + '<h1>IN<h1/>' + '<br/>' +\
        '<h1>' + request.user.username + '<h1/>' + '<a href="../"><h1>LOGOUT<h1/></a>'
    return HttpResponse(html)

def logout(request):
    logout(request)

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/you_are_in/')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})
