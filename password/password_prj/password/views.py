import random
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def result(request):
    length = request.GET.get('fulltext')

    if not length:
        return render(request, 'error2.html')
    
    try:
        number = int(length)

        if number < 0:
            return render(request, 'error1.html')
        
        else:
            return render(request, 'result.html')
    
    except:
        return render(request, '')


def error1(request):
    return render(request, 'error1.html')

def error2(request):
    return render(request, 'error2.html')

def error3(request):
    return render(request, 'error3.html')

def password_generator(request):
    length = request.GET.get('fulltext')

    if not length:
        return render(request, 'error2.html')
    
    try:
        number = int(length)

        if number < 0:
            return render(request, 'error1.html')
    
        EL = 'ES' in request.GET
        ES = 'ES' in request.GET
        num = 'num' in request.GET
        spe = 'spe' in request.GET

        check_chars = ''
        if EL:
            check_chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if ES:
            check_chars += 'abcdefghijklmnopqrstuvwxyz'
        if num:
            check_chars += '0123456789'
        if spe:
            check_chars += '!@#$%^&*'

        if not check_chars:
            return render(request, 'error3.html')

        password = ''
        for _ in range(number):
            password += random.choice(check_chars)
        return render(request, 'result.html', {'password': password})
    
    except ValueError:
        return render(request, 'error1.html')
    