from django.shortcuts import render,redirect, get_object_or_404
from .models import Post
from django.db.models import Q

def list(request):
    posts=Post.objects.all().order_by('-created_at')
    return render(request,'list.html',{'posts':posts})


def result(request ):
    keyword=request.GET.get('keyword','').strip()
    posts= Post.objects.filter(Q(title__icontains=keyword) | Q(content__icontains=keyword)).order_by('-created_at')
    

    return render(request, 'result.html', {
        'posts': posts,
        'keyword':keyword,
        })

def create(request):
    if request.method=='POST':
        title=request.POST.get('title')
        content = request.POST.get('content')

        post=Post.objects.create(title=title, content=content)
        return redirect('posts:list')
    return render(request, 'create.html')

def detail(request, id):
    post=get_object_or_404(Post, id=id)
    post.count_views()

    return render(request, 'detail.html', {'post': post})

def update(request, id):
    post=get_object_or_404(Post, id=id)

    if request.method == 'POST':
        post.title=request.POST.get('title')
        post.content=request.POST.get('content')
        post.save()
        return redirect('posts:detail', id)
    return render(request, 'update.html', {'post': post})

def delete(request, id):
    post=get_object_or_404(Post, id=id)
    post.delete()
    return redirect('posts:list')