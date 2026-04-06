from django.shortcuts import render, redirect, get_object_or_404
from .models import Phone
from django.views.generic import ListView


class IndexView(ListView):
    queryset=Phone.objects.all().order_by('name') 
    template_name='list.html'
    context_object_name='phones'


def result(request):
    keyword = request.GET.get('keyword', '').strip()
    phones = Phone.objects.filter(name__contains=keyword).order_by('name')

    return render(request, 'result.html', {
        'phones': phones,
        'keyword': keyword,
    })

def create(request):
    if request.method =='POST':
        name = request.POST.get('name')
        phone_num = request.POST.get('phone_num') 
        email = request.POST.get('email')

        phone = Phone.objects.create(
            name = name,
            phone_num = phone_num,
            email = email
        )
        return redirect('phone:list')
    return render(request, 'create.html')

def delete(request,id):
    phone=get_object_or_404(Phone, id=id)
    
    if request.method == "POST":
        phone.delete()
        return redirect('phone:list')
    return render(request, 'delete.html', {'phone':phone})

def detail(request, id):
    phone=get_object_or_404(Phone, id=id)
    return render(request, 'detail.html', {'phone':phone})

def update(request,id):
    phone=get_object_or_404(Phone, id=id)
    if request.method=='POST':
        phone.name=request.POST.get('name')
        phone.phone_num=request.POST.get('phone_num') 
        phone.email=request.POST.get('email')
        phone.save()

        return redirect('phone:detail', id)

    return render(request, 'update.html', {'phone':phone})
