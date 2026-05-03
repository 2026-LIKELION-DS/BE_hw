# posts/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment

def main(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            title = request.POST.get('title')
            content = request.POST.get('content')
            is_checked = request.POST.get('is_anoymouse') == 'on'
            Post.objects.create(
                title=title, content=content,
                author=request.user, is_anoymouse=is_checked 
            )
        return redirect('posts:main')
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/main.html', {'posts': posts})

def detail(request, id):
    post = get_object_or_404(Post, id=id)
    comments = post.comments.all().order_by('created_at')
    return render(request, 'posts/detail.html', {'post': post, 'comments': comments})

def post_delete(request, id): 
    post = get_object_or_404(Post, id=id)
    if request.user == post.author:
        post.delete()
    return redirect('posts:main')

def comment_create(request, id):
    if request.method == 'POST' and request.user.is_authenticated:
        post = get_object_or_404(Post, id=id)
        Comment.objects.create(
            post=post, author=request.user,
            content=request.POST.get('content'),
            is_anoymouse=request.POST.get('is_anoymouse') == 'on'
        )
    return redirect('posts:detail', id=id)

def comment_delete(request, com_id):
    comment = get_object_or_404(Comment, id=com_id)
    post_id = comment.post.id
    if request.user == comment.author:
        comment.delete()
    return redirect('posts:detail', id=post_id)

def post_update(request, id):
    post = get_object_or_404(Post, id=id)
    
    if request.user != post.author:
        return redirect('posts:detail', id=post.id)

    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.is_anoymouse = request.POST.get('is_anoymouse') == 'on'
        post.save()
        return redirect('posts:detail', id=post.id)
    
    return render(request, 'posts/update.html', {'post': post})