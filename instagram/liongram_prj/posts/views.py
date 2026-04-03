from django.shortcuts import render
from .models import Post
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

def detail(request, id):
    post = get_object_or_404(Post, id=id)

    post.views += 1
    post.save()

    return render(request, 'posts/detail.html', {'post':post})

def list(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'posts/list.html', {'posts':posts})


def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        Post.objects.create(
            title=title,
            content=content
        )

        return redirect('posts:list')

    return render(request, 'posts/create.html')

def update(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()   

        return redirect('posts:detail', id)  

    return render(request, 'posts/update.html', {'post': post})

def delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('posts:list')


def result(request):
    query = request.GET.get('query', '').strip()

    if query:
        posts = Post.objects.filter(
            Q(title__contains=query) | Q(content__contains=query)  
        ).order_by('title')
    else:
        posts = Post.objects.all().order_by('title')

    return render(request, 'posts/result.html', {
        'posts': posts,
        'query': query
    })