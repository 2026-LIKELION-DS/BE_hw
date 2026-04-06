from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.db.models import Q  # Q 객체 임포트
# Create your views here.

def list(request):
    posts = Post.objects.all().order_by('-created_at') # 최신순 정렬
    return render(request, 'posts/list.html',{'posts':posts})

def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        post = Post.objects.create(
            title = title,
            content = content,
        )
        
        return redirect('posts:list') # render와 redirect 차이
    return render(request, 'posts/create.html')


def detail(request, id):
    post = get_object_or_404(Post, id=id)
    post.update_views()  # 모델에 정의된 함수 - 조회수 증가 반영
    return render(request, 'posts/detail.html', {'post':post})


def result(request):
    keyword = request.GET.get('keyword')
    
    results = Post.objects.filter(
        Q(title__contains=keyword) | Q(content__contains=keyword)
    ).order_by('-created_at')
    
    return render(request, 'posts/result.html',{'results':results, 'keyword':keyword})


def update(request, id):
    post = get_object_or_404(Post, id=id)
    
    if request.method == "POST":
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('posts:detail', id = id) 
    return render(request, 'posts/update.html', {'post':post})

def delete(request, id):
    post= get_object_or_404(Post, id=id)
    post.delete()
    return redirect('posts:list')
