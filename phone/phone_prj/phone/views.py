from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.views.generic import ListView

class PhoneListView(ListView):
    ueryset = Post.objects.all().order_by('name')
    template_name = 'phone/phone_list.html'
    context_object_name = 'posts'
    model = Post

def result(request):
    query = request.GET.get('name')

    if query:
        posts = Post.objects.filter(name__contains=query).order_by('name')
    else:
        posts = Post.objects.all().order_by('name')

    return render(request, 'phone/result.html', {'posts': posts,'query': query
    })   

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')
        email = request.POST.get('email')

        Post.objects.create(
            name=name,
            number=number,
            email=email
        )
        return redirect('phone:phone_list')

    return render(request, 'phone/create.html')

def delete(request, id):
    phone = Post.objects.get(id=id)
    if request.method == 'POST':
        phone.delete()
        return redirect('phone:phone_list')
    return render(request, 'phone/delete.html', {'phone': phone})

def detail(request, id):
    post = get_object_or_404(Post, id=id)


    return render(request, 'phone/detail.html', {'post':post})

def update(request, id):
    phone = Post.objects.get(id=id)

    if request.method == 'POST':
        phone.name = request.POST.get('name')
        phone.number = request.POST.get('number')
        phone.email = request.POST.get('email')
        phone.save()
        return redirect('phone:detail', phone.id)

    return render(request, 'phone/update.html', {'phone': phone})