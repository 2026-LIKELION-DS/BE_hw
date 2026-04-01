from django.shortcuts import render, redirect
from .models import Phone
from django.shortcuts import get_object_or_404
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# Create your views here.
def list(request):
    phones = Phone.objects.all().order_by('name')
    return render(request, 'phone/list.html', {'phones': phones})

def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone_num = request.POST.get('phone_num')
        email = request.POST.get('email')

        try:
            validate_email(email)

            Phone.objects.create(
                name=name, 
                phone_num=phone_num, 
                email=email
            )
            return redirect('phone:list')
        
        except ValidationError:
            return render(request, 'phone/create.html', {
                'error': 'Enter a valid email address.',
                'name' : name,
                'phone_num' : phone_num, 
            })

        phone = Phone.objects.create(
            name = name,
            phone_num = phone_num,
            email = email, 
        )
        return redirect('phone:list')
    return render(request, 'phone/create.html')

def detail(request, id):
    phone = get_object_or_404(Phone, id=id)
    return render(request, 'phone/detail.html', {'phone':phone})

def update(request, id):
    phone = get_object_or_404(Phone, id=id)

    if request.method == 'PHONE':
        phone.name = request.PHONE.get('name')
        phone.phone_num = request.PHONE.get('phone_num')
        phone.save()
        return redirect('phone:datail', id)
    return render(request, 'phone/update.html', {'phone':phone})

def result(request):
    query = request.GET.get('keyword')

    if query:
        phones = Phone.objects.filter(name__icontains=query).order_by('name')
    else:
        phones = Phone.objects.none()

    return render(request, 'phone/result.html', {'phones': phones, 'keyword':query})
