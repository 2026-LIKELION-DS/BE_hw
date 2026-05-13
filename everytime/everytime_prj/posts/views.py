from django.shortcuts import render, redirect
from .models import Post, Comment, Category, PostCategory, Like, Scrap
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

def main(request):
    categories = Category.objects.all()
    category_posts = []
    for category in categories:
        posts = Post.objects.filter(category=category).order_by('-created_at')[:4]
        category_posts.append({'category': category, 'posts': posts})
    return render(request, 'posts/main.html', {'category_posts': category_posts})

def detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all().order_by('created_at')

    if request.method == 'POST':
        content = request.POST.get('content')
        is_anonymous = request.POST.get('is_anonymous') == 'on'
        image = request.FILES.get('image')
        video = request.FILES.get('video') 
        
        Comment.objects.create(
            post=post,
            author=request.user,
            content=content,
            is_anonymous=is_anonymous,
            image=image,
            video=video 
            
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
        image = request.FILES.get('image') 
        video = request.FILES.get('video')
        
        if image:
            post.image.delete()
            post.image = image
        if video:
            post.video.delete()
            post.video = video
        
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

def category(request, slug):
    cat = get_object_or_404(Category, slug=slug)

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        is_anonymous = request.POST.get('is_anonymous') == 'on'
        image = request.FILES.get('image')   
        video = request.FILES.get('video') 
        
        post = Post.objects.create(
            title=title,
            content=content,
            is_anonymous=is_anonymous,
            author=request.user,
            image=image,
            video=video 
        )
        post.category.add(cat)
        return redirect('posts:category', slug=slug)

    posts = Post.objects.filter(category=cat).order_by('-created_at')
    return render(request, 'posts/category.html', {'category': cat, 'posts': posts})

@login_required
def like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        like_obj = Like.objects.filter(post=post, user=request.user)
        if like_obj.exists():
            like_obj.delete()
        else:
            Like.objects.create(post=post, user=request.user)
    return redirect('posts:detail', post_id=post_id)

@login_required
def scrap(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        scrap_obj = Scrap.objects.filter(post=post, user=request.user)
        if scrap_obj.exists():
            scrap_obj.delete()
        else:
            Scrap.objects.create(post=post, user=request.user)
    return redirect('posts:detail', post_id=post_id)

