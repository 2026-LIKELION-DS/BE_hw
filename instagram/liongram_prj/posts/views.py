from django.shortcuts import render, redirect
from .models import Post
from django.db.models import Q
from django.views.generic import ListView

class IndexView(ListView):
    queryset = Post.objects.all().order_by("-id")
    template_name = "posts/list.html"
    context_object_name = "posts"

def create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        Post.objects.create(title=title, content=content)
        return redirect("posts:list") 
    return render(request, "posts/create.html")

def detail(request, id):
    post = Post.objects.get(id=id)
    post.view_count += 1
    post.save()
    return render(request, "posts/detail.html", {"post": post})

def update(request, id):
    post = Post.objects.get(id=id)
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        post.title = title
        post.content = content
        post.save()
        return redirect("posts:detail", id=id)
    return render(request, "posts/update.html", {"post": post})

def delete(request, id):
    post = Post.objects.get(id=id)
    if request.method == "POST":
        post.delete()
    return redirect("posts:list")  

def result(request):
    search = request.GET.get("search")
    posts = Post.objects.filter(Q(title__contains=search) | Q(content__contains=search)).order_by("-id")
    if not posts:
        posts = None
    return render(request, "posts/result.html", {"posts": posts, "search": search})
