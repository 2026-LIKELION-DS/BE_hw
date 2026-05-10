from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, Category, PostCategory
from django.contrib.auth.decorators import login_required

@login_required
def main(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    return render(request, 'posts/main.html', {'categories':categories, 'posts':posts})

def detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'posts/detail.html', {'post': post})

def update(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.is_anonymous = (request.POST.get('anonymous') == 'on')
        post.save()
        return redirect('posts:detail', id=id)

    return render(request, 'posts/update.html', {'post': post})

def delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('posts:main')

def comment(request, comment_id):
    post = get_object_or_404(Post, id=comment_id)
    if request.method == "POST":
        content = request.POST.get('content')
        anonymous = request.POST.get('anonymous')

        Comment.objects.create(
            post=post,
            content=content,
            is_anonymous = True if anonymous == 'on' else False,
            author=request.user.nickname
        )
        return redirect('posts:detail', comment_id)
    
def comment_delete(request, post_id):
    comment = get_object_or_404(Comment, id=post_id)
    post_id = comment.post.id

    comment.delete()
    
        
    return redirect('posts:detail',post_id)


def category_detail(request, slug):
    current_category = get_object_or_404(Category, slug=slug)

    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        anonymous = request.POST.get('anonymous')
        is_anonymous = True if anonymous == 'on' else False
        image = request.FILES.get('image')
        video = request.FILES.get('video')

        new_post = Post.objects.create(
            title = title,
            content = content,
            image=image,
            video=video,
            is_anonymous = is_anonymous,
            author = request.user.username
        )

        PostCategory.objects.create(posts=new_post, category=current_category)
        return redirect('posts:category_detail', slug=slug)
    
    posts = Post.objects.filter(category=current_category).order_by('-id')

    return render(request, 'posts/category.html', {
        'category' : current_category, 
        'posts' : posts
    })


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