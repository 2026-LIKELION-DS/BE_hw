from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, Category
from django.shortcuts import get_object_or_404

# Create your views here.
def main(request):
    categories = Category.objects.all()
    # 카테고리별 최신 글 4개씩 묶어서 넘기기!!
    category_posts = []
    for category in categories:
        posts = category.posts.all().order_by('-created_at')[:4]
        category_posts.append({
            'category': category,
            'posts': posts,
        })
    return render(request, 'posts/main.html', {'category_posts': category_posts})


@login_required
def create(request, slug): # slug를 받아서 해당 카테고리로 글 등록
    category = get_object_or_404(Category, slug=slug)
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        is_anonymous = request.POST.get('is_anonymous') == "on"
        image = request.FILES.get('image')
        video = request.FILES.get('video')
        
        post = Post.objects.create(
            title = title,
            content = content,
            author = request.user,
            is_anonymous = is_anonymous,
            image = image,
            video = video
        )
        post.category.add(category) # 해당 카테고리 연결
        return redirect('posts:category_list',slug=slug)
    return render(request, 'posts/create.html', {'category':category})

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
        image = request.FILES.get('image')
        video = request.FILES.get('video')
        
        if image:
            post.image.delete()
            post.image = image
            
        if video:
            post.video.delete()
            post.video = video
        
        
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

def category_list(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.all().order_by('-id')
    return render(request, 'posts/category.html', {'category': category,'posts': posts})



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