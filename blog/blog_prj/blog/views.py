from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, Category
from django.contrib.auth.decorators import login_required


# Create your views here.
def list(request):
    categories = Category.objects.all()
    category_id = request.GET.get('category')
    
    if category_id:
        # category = get_object_or_404(Category, id=category_id)
        # posts = category.posts.all().order_by('-id')
        posts = Post.objects.filter(category__id=category_id).order_by('-id')
    else:
        posts = Post.objects.all().order_by('-id')
        
    return render(request, 'blog/list.html', {'posts':posts, 'categories':categories})


@login_required
def create(request):  # 7차세션 - 헷갈리기 쉬우니까 코드 흐름 정리
    categories = Category.objects.all()
    
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        video = request.FILES.get('video')
        
        category_ids = request.POST.getlist('category')
        category_list = [get_object_or_404(Category, id=category_id) for category_id in category_ids]
        
        post = Post.objects.create(
            title = title,
            content = content,
            author = request.user,  # 로그인한 사용자를 게시글의 작성자로 저장
            image = image,
            video = video,
        )
        
        for category in category_list:
            post.category.add(category)
        
        return redirect('blog:list') # render와 redirect 차이
    return render(request, 'blog/create.html',{'categories':categories})

def detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/detail.html', {'post':post})

def update(request, id):
    post = get_object_or_404(Post, id=id)
    
    if request.method == "POST":
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
        return redirect('blog:detail',id=post.id)
    
    return render(request, 'blog/update.html', {'post':post})

def delete(request, id):
    post= get_object_or_404(Post, id=id)
    post.delete()
    return redirect('blog:list')


@login_required
def create_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        
        Comment.objects.create(
            post = post,
            content = content,
            author = request.user
        )
        return redirect('blog:detail', post_id)
    return redirect('blog:list')


def like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user
    
    # if user in post.like.all():  # 정참조 방식
    #     post.like.remove(user)
    # else:
    #     post.like.add(user)
    
    if post in user.like_posts.all():  # 역참조 방식
        user.like_posts.remove(post)
        
    else:
        user.like_posts.add(post)
    
    return redirect('blog:detail', post_id)    
    