from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from django.contrib.auth.decorators import login_required


def main(request):
    if request.method == "POST":
        Post.objects.create(
            title = request.POST.get('title'),
            content = request.POST.get('content'),
            author = request.user,
            is_anonymous = request.POST.get('anonymous') == 'on'
        )
        return redirect('posts:main')
    posts = Post.objects.all().order_by('id')
    return render(request, 'posts/main.html', {'posts':posts})

def detail(request, post_id):
    post = get_object_or_404(Post, id=post_id) 
    return render(request, 'posts/detail.html', {'post': post})

@login_required
def update(request, post_id):
    post = get_object_or_404(Post, id = post_id)

    if post.author != request.user:
        return redirect('posts:main')
    
    if request.method == "POST":
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.is_anonymous = request.POST.get('anonymous') == 'on'
        post.save()
        return redirect('posts:detail', post_id = post.id)
    return render(request, 'posts/update.html', {'post':post})

@login_required
def delete(request, post_id):
    post = get_object_or_404(Post, id = post_id)
    if post.author == request.user:
        post.delete()

    return redirect('posts:main')

@login_required
def comment_create(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        Comment.objects.create(
            post = post,
            author = request.user,
            content = request.POST.get('content'),
            is_anonymous = request.POST.get('anonymous') == 'on'
        )
    return redirect('posts:detail', post_id=post.id)

@login_required
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    post_id = comment.post.id

    if comment.author == request.user:
        comment.delete()
        return redirect('posts:detail', post_id=post_id)
    else:
        return redirect('posts:main')

