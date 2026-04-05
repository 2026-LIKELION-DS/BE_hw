from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.db.models import Q

# Create your views here.
def list(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'posts/list.html', {'posts': posts})

def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        views = 0
        created_at = request.POST.get('created_at')

        post = Post.objects.create(
            title = title,
            content = content,
            views = views,
            created_at = created_at
        )
        return redirect('posts:list')
    return render(request, 'posts/create.html')

def detail(request, id):
    post = get_object_or_404(Post, id=id)

    post.views = post.views + 1
    post.save()
    return render(request, 'posts/detail.html', {'post': post})

def update(request, id):
    post =get_object_or_404(Post, id=id)

    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('posts:detail', id)
    return render(request, 'posts/update.html', {'post':post})

def delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('posts:list')

def result(request):
    query = request.GET.get('keyword')

    if query:
        posts = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query)).distinct().order_by('-created_at')
    else:
        posts = Post.objects.none()

    return render(request, 'posts/result.html', {'posts': posts, 'keyword':query})