import random
from django.shortcuts import render

def index(request):

    return render(request, 'password/index.html')
# Create your views here.


def password_generation(request):
    length = request.GET.get("length")
    upper = "upper" in request.GET
    lower = "lower" in request.GET
    digits = "digits" in request.GET
    special = "special" in request.GET

    if not length:
        return render(request, 'password/error2.html')
    
    length = int(length)

    if length <= 0:
        return render(request, 'password/error1.html')

    if not (upper or lower or digits or special):
        return render(request, 'password/error3.html')
    
    check_chars = ""
    if upper:
        check_chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if lower:
        check_chars += "abcdefghijklmnopqrstuvwxyz"
    if digits:
        check_chars += "0123456789"
    if special:
        check_chars += "!@#$%^&*"

    password = ""
    for i in range(length):
        picked_chars = random.choice(check_chars)
        password += picked_chars

    return render(request,'password/result.html', {'password' : password})