from django.shortcuts import render, redirect
from .models import Post, Comment, Category
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
def main(request):
    secret_posts = Post.objects.filter(category__slug='secret').order_by('-created_at')[:4]
    freshman_posts = Post.objects.filter(category__slug='freshman').order_by('-created_at')[:4]
    free_posts = Post.objects.filter(category__slug='free').order_by('-created_at')[:4]

    return render(request, 'posts/main.html', {'secret_posts': secret_posts, 'freshman_posts': freshman_posts, 'free_posts': free_posts})

def list(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'everytime/list.html', {'posts': posts})

@login_required
def create(request, slug):
    category = Category.objects.get(slug=slug)

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        is_anonymous = request.POST.get('is_anonymous') == 'on'
        image = request.FILES.get('image')
        video = request.FILES.get('video')

        posts = Post.objects.create(
            title = title,
            content = content,
            author = request.user,
            is_anonymous = is_anonymous,
            category = category,
            image = image,
            video = video
        )
        return redirect('posts:category', slug=slug)
    posts = Post.objects.filter(category=category).order_by('-created_at')
    return render(request, 'posts/category.html', {'category':category, 'posts': posts})

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
        image = request.FILES.get('image')
        video = request.FILES.get('video')

        if image:
            post.image.delete()
            post.image = image
        
        if video:
            post.video.delete()
            post.video = video
            
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

def category(request, slug):
    category = Category.objects.get(slug=slug)
    posts = Post.objects.filter(category=category).order_by('-created_at')

    return render(request, 'posts/category.html', {'category':category, 'posts':posts})

def like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user

    if user in post.like.all():
        post.like.remove(user)
    else:
        post.like.add(user)
    return redirect('posts:detail', post_id)

def scrap(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user

    if user in post.scrap.all():
        post.scrap.remove(user)
    else:
        post.scrap.add(user)
    return redirect('posts:detail', post_id)