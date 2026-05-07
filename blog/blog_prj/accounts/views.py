from django.shortcuts import render, redirect
from .forms import *
from blog.models import Post
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

def signup(request):
    if request.method == 'GET':
        form = SignUpForm()
        return render(request, 'accounts/signup.html', {'form': form})

    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('accounts:login')
    else:
        return render(request, 'accounts/signup.html', {'form': form})
    

def login(request):
    if request.method == 'GET':
        return render(request, 'accounts/login.html', {'form': AuthenticationForm()})
    
    form = AuthenticationForm(request, request.POST)
    if form.is_valid():
        auth_login(request, form.user_cache)
        return redirect('blog:list')
    return render(request, 'accounts/login.html', {'form': form})


from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect

def logout(request):
    auth_logout(request)
    return redirect('blog:list')

def mypage(request):
    return render(request, 'accounts/mypage.html')

def user_info(request):
    return render(request, 'accounts/user_info.html')

def myblog(request):
    posts=Post.objects.filter(user=request.user).order_by('-id')
    return render(request, 'accounts/myblog.html', {'posts':posts})

def mylike(request):

    liked_posts = Post.objects.filter(like=request.user).order_by('-id')

    return render(request, 'accounts/mylike.html', {'liked_posts': liked_posts})