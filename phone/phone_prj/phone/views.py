from django.shortcuts import render, redirect
from .models import Phone
from django.shortcuts import get_object_or_404
from django.views.generic import ListView

class IndexView(ListView):
    queryset = Phone.objects.all().order_by('name')
    template_name = 'phone/list.html'
    context_object_name = 'phones'

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_num = request.POST.get('phone_num')
        email = request.POST.get('email')

        phone = Phone.objects.create(
            name=name,
            phone_num=phone_num,
            email=email
        )
        return redirect('phone:list')
    return render(request, 'phone/create.html')

def detail(request, id):
    phone = get_object_or_404(Phone, id=id)
    return render(request, 'phone/detail.html', {'phone' : phone})

def result(request):
    # 사용자가 입력한 검색어 가져오기
    search_word = request.GET.get('search') 

    phones = Phone.objects.filter(name__contains=search_word).order_by('name')
    return render(request, 'phone/result.html', {'phones': phones, 'search_word': search_word})

def update(request, id):
    phone = get_object_or_404(Phone, id=id)

    if request.method == 'POST':
        phone.name = request.POST.get('name')
        phone.phone_num = request.POST.get('phone_num')
        phone.email = request.POST.get('email')
        phone.save()
        return redirect('phone:detail', id)
    return render(request, 'phone/update.html', {'phone':phone})

def delete(request, id):
    phone = get_object_or_404(Phone, id=id)

    if request.method == 'POST':
        phone.delete()
        return redirect('phone:list')
    return render(request, 'phone/delete.html', {'phone':phone})
    
