from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from  .models import Post

def list(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'posts/list.html', {'posts':posts})

def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')

        post = Post.objects.create(
            title = title,
            content = content
        )
        return redirect('posts:list')
    return render(request, 'posts/create.html')

def detail(request, id):
    post = get_object_or_404(Post, id=id)
    post.views += 1
    post.save()
    return render(request, 'posts/detail.html', {'post': post})

def update(request,id):
    post = get_object_or_404(Post, id=id)
    
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('posts:list')
    return render(request, 'posts/update.html', {'post': post})


def delete(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        post.delete()
        return redirect('posts:list')

    return redirect('posts:detail', id=id)

def search(request):
    keyword = request.GET.get('keyword')
    results = []

    if keyword:
        results = Post.objects.filter(
            Q(title__icontains=keyword) | Q(content__icontains=keyword)
        ).order_by('-id')

    return render(request, 'posts/result.html', {
        'posts': results, 
        'keyword': keyword
    })