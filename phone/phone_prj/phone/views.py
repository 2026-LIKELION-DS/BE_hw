from django.shortcuts import render
from .models import Post

def list(request):
    posts = Post.objects.all().order_by('name')
    return render(request, 'phone/list.html', {'posts':posts})

def result(request):
    query = request.GET.get('name')

    if query:
        posts = Post.objects.filter(name__contains=query).order_by('name')
    else:
        posts = Post.objects.all().order_by('name')

    return render(request, 'phone/result.html', {'posts': posts,'query': query
    })   
