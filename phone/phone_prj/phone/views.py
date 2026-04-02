from django.shortcuts import render, redirect
from .models import Phone
from django.shortcuts import get_object_or_404
from django.db.models import Q  

def list(request):
    phones = Phone.objects.all().order_by('name')
    return render(request, 'phone/list.html', {'phones': phones})

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

    if search_word:
        posts = Phone.objects.filter(Q(name__contains=search_word) | Q(phone_num__contains=search_word))
    else:
        posts = Phone.objects.none() # 검색어가 없으면 빈 결과 반환

    return render(request, 'phone/result.html', {'posts': posts, 'search_word': search_word})
