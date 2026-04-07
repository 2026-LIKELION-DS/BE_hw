from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Post
from django.db.models import Q 

def list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/list.html', {'posts':posts})

def detail(request, id):
    post = get_object_or_404(Post, id = id)

    post.update_views()

    return render(request, 'posts/detail.html', {'post':post})

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

def update(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == "POST":
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('posts:detail', id=post.id)
    return render(request, 'posts/update.html', {'post':post})

def delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('posts:list')

def result(request):
    search_word = request.GET.get('search') 

    if search_word:
        posts = Post.objects.filter(Q(title__icontains=search_word) | Q(content__icontains=search_word)).order_by('-created_at')
    else:
        posts = Post.objects.none() 

    return render(request, 'posts/result.html', {'posts': posts, 'search_word': search_word})


