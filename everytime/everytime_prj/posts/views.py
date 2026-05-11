from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, Category, PostCategory
from django.contrib.auth.decorators import login_required


def main(request):
    categories = Category.objects.all()

    if request.method == "POST":
        post = Post.objects.create(
            title = request.POST.get('title'),
            content = request.POST.get('content'),
            author = request.user,
            is_anonymous = request.POST.get('anonymous') == 'on'
        )

        category_ids = request.POST.getlist('category')
        for category_id in category_ids:
            category = get_object_or_404(Category, id = category_id) 
            post.category.add(category)
        return redirect('posts:main')
    return render(request, 'posts/main.html', {'categories': categories})

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
        if request.FILES.get('image'):
            post.image = request.FILES.get('image')
            
        if request.FILES.get('video'):
            post.video = request.FILES.get('video')
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
    

def category_detail(request, slug):
    category = get_object_or_404(Category, slug = slug)

    if request.method == "POST":
        post = Post.objects.create(
            title = request.POST.get('title'),
            content = request.POST.get('content'),
            author = request.user,
            is_anonymous = request.POST.get('anonymous') == 'on',
            image = request.FILES.get('image'),
            video = request.FILES.get('video'),
        )
        post.category.add(category)
        return redirect('posts:category_detail', slug = slug)
    posts = category.posts.all().order_by('-created_at')
    return render(request, 'posts/category.html',{
        'category': category,
        'posts' : posts,
    })

def post_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user) 
    else:
        post.likes.add(request.user)   
    return redirect('posts:detail', post_id=post.id)

def post_scrap(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.scraps.filter(id=request.user.id).exists():
        post.scraps.remove(request.user)
    else:
        post.scraps.add(request.user)   
    return redirect('posts:detail', post_id=post.id)



