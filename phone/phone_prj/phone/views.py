from django.shortcuts import render, redirect
from  .models import Contact

def list(request):
    contacts = Contact.objects.all().order_by('name')
    return render(request, 'phone/list.html', {'contacts':contacts})

def search_result(request):
    keyword = request.GET.get('keyword', '')
    
    if keyword:
        results = Contact.objects.filter(name__contains=keyword).order_by('name')
    else:
        results = Contact.objects.none()

    return render(request, 'phone/result.html', {
        'results': results, 
        'keyword': keyword
    })

def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone_num = request.POST.get('phone_num')
        email = request.POST.get('email')

        POST = Contact.objects.create(
            name = name,
            phone_num = phone_num,
            email = email
        )
        return redirect('phone:list')
    return render(request, 'phone/create.html')