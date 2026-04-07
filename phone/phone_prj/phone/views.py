from django.shortcuts import render, redirect
from .models import Phone
from django.db.models import Q
from django.views.generic import ListView

class IndexView(ListView):
    queryset = Phone.objects.all().order_by("name")
    template_name = "phone/list.html"
    context_object_name = "phones"

def create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone_num = request.POST.get("phone_num")
        email = request.POST.get("email")
        
        phone = Phone.objects.create(
            name = name,
            phone_num = phone_num,
            email = email
        )
        return redirect('phone:list')
    return render(request, "phone/create.html")

def result(request):
    keyword = request.GET.get("keyword")
    phones = Phone.objects.filter(name__contains=keyword).order_by('name')
    
    return render(request, "phone/result.html", {"phones": phones, "keyword": keyword})

def detail(request,id):
    phone = Phone.objects.get(id=id)
    return render(request, "phone/detail.html", {"phone": phone})

def delete(request,id):
    phone = Phone.objects.get(id=id)
    if request.method == "POST":
        phone.delete()
        return redirect('phone:list')
    return render(request, "phone/delete.html", {"phone": phone})

def update(request,id):
    phone = Phone.objects.get(id=id)
    if request.method == "POST":
        phone.name = request.POST.get("name")
        phone.phone_num = request.POST.get("phone_num")
        phone.email = request.POST.get("email")
        phone.save()
        return redirect('phone:detail', id=id)
    return render(request, "phone/update.html", {"phone": phone})