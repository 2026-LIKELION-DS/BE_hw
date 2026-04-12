from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.contrib.auth.decorators import login_required


def list(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'everytime/list.html', {'posts': posts})

@login_required
def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        Post.objects.create(title=title, content=content)
        return redirect('everytime:list')
    
    return render(request, 'everytime/create.html')


def detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'everytime/detail.html', {'post': post})


def update(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('everytime:detail', id=id)

    return render(request, 'everytime/update.html', {'post': post})

def delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('everytime:list')