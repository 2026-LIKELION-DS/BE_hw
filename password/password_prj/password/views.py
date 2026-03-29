import random
import string
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def generation(length, use_upper, use_lower, use_number, use_special):
    check_chars = ""

    if use_upper:
        check_chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if use_lower:
        check_chars += "abcdefghijklmnopqrstuvwxyz"
    if use_number:
        check_chars += "0123456789"
    if use_special:
        check_chars += "!@#$%^&*"

    password = ''.join(random.choice(check_chars) for _ in range(length))
    return password


def result(request):
    length = request.GET.get('length')

    if not length:
        return render(request, 'error1.html')

    try:
        length = int(length)
    except ValueError:
        return render(request, 'error1.htmi')

    if length <= 0:
        return render(request, 'error2.html')

    use_upper = 'upper' in request.GET
    use_lower = 'lower' in request.GET
    use_digits = 'digits' in request.GET
    use_special = 'special' in request.GET

    if not (use_upper or use_lower or use_digits or use_special):
        return render(request, 'error3.html')

    password = generation(length, use_upper, use_lower, use_digits, use_special)
    return render(request, 'result.html', {'password': password})