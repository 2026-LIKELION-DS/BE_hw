from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, 'password/index.html')

def password_generator(request):
    length = request.GET.get('length')
    upper = request.GET.get('upper')
    lower = request.GET.get('lower')
    number = request.GET.get('number')
    special = request.GET.get('special')
    
    #추가: 모두 선택 X
    if not length and not upper and not lower and not number and not special:
        return render(request, 'password/error4.html')
    
    #입력 X
    if not length:
        return render(request, 'password/error1.html')
    #음수값 입력
    if int(length) < 0:
        return render(request, 'password/error2.html')
    #체크박스 X
    if not upper and not lower and not number and not special:
        return render(request, 'password/error3.html')
    
    
    #문서 set 구성
    check_chars = ""
    if upper:
        check_chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if lower:
        check_chars += "abcdefghijklmnopqrstuvwxyz"
    if number:
        check_chars += "0123456789"
    if special:
        check_chars += "!@#$%^&*()-+"
    
    
    #비밀번호 생성
    password = ""
    for i in range(int(length)):
        random_char = random.choice(check_chars)
        password = password + random_char
    
    return render(request, 'password/result.html', {'password': password})