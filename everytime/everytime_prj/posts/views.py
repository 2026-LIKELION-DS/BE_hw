from django.shortcuts import render, redirect
from .models import Post, Comment
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

def main(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        is_anonymous = request.POST.get('is_anonymous') == 'on'
        
        Post.objects.create(
            title=title, 
            content=content, 
            is_anonymous=is_anonymous,
            author=request.user
        )
        return redirect('posts:main')
    
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/main.html', {'posts': posts})

def detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all().order_by('created_at')

    if request.method == 'POST':
        content = request.POST.get('content')
        is_anonymous = request.POST.get('is_anonymous') == 'on'
        
        Comment.objects.create(
            post=post,
            author=request.user,
            content=content,
            is_anonymous=is_anonymous
        )
        return redirect('posts:detail', post_id=post_id)
    
    return render(request, 'posts/detail.html', {'post': post, 'comments': comments})

def update(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if request.user != post.author:
        return redirect('posts:detail', post_id=post_id)
    
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.is_anonymous = request.POST.get('is_anonymous') == 'on'
        post.save()
        return redirect('posts:detail', post_id=post_id)
    
    return render(request, 'posts/update.html', {'post': post})

@login_required
def delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user == post.author:
        post.delete()
    return redirect('posts:main')

@login_required
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    post_id = comment.post.id
    if request.user == comment.author:
        comment.delete()
    return redirect('posts:main')

