from django.shortcuts import render, redirect
from  .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout #우리가 만든 logout과 겹치지 않게 별칭으로 설정
from blog.models import Post

def signup(request):
    if request.method == 'GET':
        form = SignUpForm()
        return render(request, 'accounts/signup.html', {'form':form})
    
    form = SignUpForm(request.POST) #제출된 데이터 받기
    if form.is_valid(): #데이터 유효성 검사
        form.save() #유효하면 데이터를 user로 저장
        return redirect('accounts:login')
    else:
        return render(request, 'accounts/signup.html', {'form':form})

def login(request):
    if request.method == 'GET': #사용자가 로그인 페이지 들어갔을 때 GET 요청
        return render(request, 'accounts/login.html', {'form': AuthenticationForm()})
    form = AuthenticationForm(request,request.POST)
    if form.is_valid():
        auth_login(request, form.user_cache)
        return redirect('blog:list')
    return render(request, 'accounts/login.html', {'form':form})     

def logout(request):
    if request.user.is_authenticated: #로그인된 사용자가 맞는 지 점검
        auth_logout(request)
    return redirect('blog:list')

def user_info(request):
    return render(request, 'accounts/user_info.html')

def mypage(request):
    return render(request, 'accounts/mypage.html')

def myblog(request):
    posts = Post.objects.filter(author=request.user).order_by('-id')
    #posts = request.user.posts.all().order_by('-id') -> 역참조
    return render(request, 'accounts/myblog.html', {'posts': posts})