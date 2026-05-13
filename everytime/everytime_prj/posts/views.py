# posts/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import *

def main(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            title = request.POST.get('title')
            content = request.POST.get('content')
            is_checked = request.POST.get('is_anonymous') == 'on'
            Post.objects.create(
                title=title, content=content,
                author=request.user, is_anonymous=is_checked 
            )
        return redirect('posts:main')

    categories = Category.objects.all() 
    posts = Post.objects.all().order_by('-created_at')

    return render(request, 'posts/main.html', {
        'posts': posts, 
        'categories': categories  
    })

def detail(request, id):
    post = get_object_or_404(Post, id=id)
    comments = post.comments.all().order_by('created_at')
    
    is_liked = post.like.filter(id=request.user.id).exists()
    is_scrapped = post.scrap.filter(id=request.user.id).exists()
    
    return render(request, 'posts/detail.html', {
        'post': post, 
        'comments': comments,
        'is_liked': is_liked,
        'is_scrapped': is_scrapped,
    })

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
            is_anonymous=request.POST.get('is_anonymous') == 'on'
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
        post.is_anonymous = request.POST.get('is_anonymous') == 'on'
        post.save()
        return redirect('posts:detail', id=post.id)
    
    return render(request, 'posts/update.html', {'post': post})

def category(request, slug):
    current_category = get_object_or_404(Category, slug=slug)
    
    if request.method == 'POST':
        if request.user.is_authenticated:
            title = request.POST.get('title')
            content = request.POST.get('content')
            is_checked = request.POST.get('is_anonymous') == 'on'
            
            new_post = Post.objects.create(
                title=title, 
                content=content,
                author=request.user, 
                is_anonymous=is_checked
            )
            new_post.category.add(current_category)
            
            return redirect('posts:category', slug=slug)

    posts = current_category.posts.all().order_by('-created_at')
    
    return render(request, 'posts/category.html', {
        'category': current_category,
        'posts': posts,
    })

def post_like(request, id):
    post = get_object_or_404(Post, id=id)
    if post.like.filter(id=request.user.id).exists():
        post.like.remove(request.user) 
    else:
        post.like.add(request.user)    
    return redirect('posts:detail', id=id)

def post_scrap(request, id):
    post = get_object_or_404(Post, id=id)
    if post.scrap.filter(id=request.user.id).exists():
        post.scrap.remove(request.user)
    else:
        post.scrap.add(request.user)   
    return redirect('posts:detail', id=id)