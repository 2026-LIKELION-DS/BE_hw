from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from django.contrib.auth.decorators import login_required

@login_required
def main(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        anonymous = request.POST.get('anonymous')
        is_anonymous = True if anonymous == 'on' else False

        Post.objects.create(title=title, content=content, is_anonymous = is_anonymous, author=request.user.username)
        return redirect('posts:main') 
    
    posts = Post.objects.all().order_by('-id')
    return render(request, 'posts/main.html', {'posts': posts})

def detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'everytime/detail.html', {'post': post})

def update(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.is_anonymous = (request.POST.get('anonymous') == 'on')
        post.save()
        return redirect('everytime:detail', id=id)

    return render(request, 'everytime/update.html', {'post': post})

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
        return redirect('everytime:detail', comment_id)
    
def comment_delete(request, post_id):
    comment = get_object_or_404(Comment, id=post_id)
    post_id = comment.post.id

    comment.delete()
    
        
    return redirect('everytime:detail',id=post_id)
