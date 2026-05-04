from django.shortcuts import render, redirect
from .models import Post, Comment
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
def main(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/main.html', {'posts': posts})

def list(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'everytime/list.html', {'posts': posts})

@login_required
def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        is_anonymous = request.POST.get('is_anonymous') == 'on'

        posts = Post.objects.create(
            title = title,
            content = content,
            author = request.user,
            is_anonymous = is_anonymous
        )
        return redirect('posts:main')
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/main.html', {'posts': posts})

def detail(request, id):
    post = get_object_or_404(Post, id=id)
    comments = post.comments.all().order_by('created_at')

    if request.method == 'POST':
        content = request.POST.get('content')
        is_anonymous = request.POST.get('is_anonymous') == 'on'

        Comment.objects.create(
            post = post,
            content = content, 
            author = request.user,
            is_anonymous = is_anonymous
        )
        return redirect('posts:detail', id)
    return render(request, 'posts/detail.html', {'post':post, 'comments': comments})

@login_required
def update(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('posts:detail', id)
    return render(request, 'posts/update.html', {'post':post})

@login_required
def delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('everytime:list')

@login_required
def comment_delete(request, id):
    comment = get_object_or_404(Comment, id=id)
    post_id = comment.post.id

    if request.user == comment.author:
        comment.delete()
    return redirect('posts:detail', post_id)