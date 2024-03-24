from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.conf import settings

from .forms import *
from .models import *


def view_news_page(request):
    news = News.objects.all()
    return render(
        request,
        'pages/news_page.html',
        {'news': news},
    )


def view_addnews_page(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        author = request.user
        title = request.POST['title']
        text = request.POST['text']
        time = timezone.now()
        new_post = News(author=author, title=title, text=text, time=time)
        new_post.save()
        return redirect('/')
    else:
        form = NewsForm()
    return render(
        request,
        'pages/addnews_page.html',
        {'form': form}
    )


def view_register_page(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        new_user = User.objects.create_user(username, email, password)
        new_user.save()
        return redirect('/')
    else:
        form = RegisterForm()
    return render(
        request,
        'pages/register_page.html',
        {'form': form}
    )


def view_login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.data['username']
            password = form.data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                '''если юзера нет'''
        else:
            '''если неккоректный ввод'''
    else:
        form = LoginForm()
    return render(
        request,
        'pages/login_page.html',
        {'form': form}
    )


def logout_page(request):
    logout(request)
    return redirect('/')


def view_profile_page(request):
    news = News.objects.all()
    user = request.user
    return render(
        request,
        'pages/profile_page.html',
        {'news': news, 'user': user},
    )