from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from django.shortcuts import get_object_or_404

# Create your views here.
def main(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/main.html',{'posts':posts})

@login_required
def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        is_anonymous = request.POST.get('is_anonymous') == "on" 
        
        Post.objects.create(
            title = title,
            content = content,
            author = request.user,
            is_anonymous = is_anonymous
        )
    return redirect('posts:main')

def detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'posts/detail.html',{'post':post})

@login_required
def update(request,post_id):
    post = get_object_or_404(Post,id=post_id)
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.is_anonymous = request.POST.get('is_anonymous') == 'on'
        post.save()
        return redirect('posts:detail', post_id=post.id)  
    return render(request, 'posts/update.html', {'post':post})

@login_required
def delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user == post.author:
        post.delete()
    return redirect('posts:main')



@login_required
def create_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if request.method == 'POST':
        content = request.POST.get('comment')
        is_anonymous = request.POST.get('is_anonymous') == 'on'
        
        Comment.objects.create(
            post = post,
            content = content,
            author = request.user,
            is_anonymous = is_anonymous,
        )
        return redirect('posts:detail', post_id=post_id)
    return redirect('posts:main')
    
@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    post_id = comment.post.id
    if request.user == comment.author:
        comment.delete()
    return redirect('posts:detail', post_id=post_id)