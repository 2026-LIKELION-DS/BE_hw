from django.shortcuts import render
from .models import Phone

def list(request):
    names = Phone.objects.all().order_by('name')

    return render(request, 'phone/list.html', {'names' : names})

def result(request):

    keyword = request.GET.get('keyword')
    
    if keyword:
        results = Phone.objects.filter(name__contains=keyword).order_by('name')
    else:
        results = Phone.objects.none()

    return render(request, 'phone/result.html', {
        'results': results, 
        'keyword': keyword
    })

