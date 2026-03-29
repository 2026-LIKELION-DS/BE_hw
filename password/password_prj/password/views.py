from django.shortcuts import render
import random

# Create your views here.

def index(request):
    return render(request, 'password/index.html')

def result(request):
    return render(request, 'password/result.html')

def error1(request):
    return render(request, 'password/error1.html')

def error2(request):
    return render(request, 'password/error2.html')

def error3(request):
    return render(request, 'password/error3.html')


def password_generator(request):
    
    length = request.GET.get('length')
    
    # 체크박스 선택 여부 확인
    upper = "upper" in request.GET
    lower = "lower" in request.GET
    digits = "digits" in request.GET 
    special = "special" in request.GET   
    
    if not length:
        return render(request, 'password/error2.html') # 비밀번호 입력 안됨
    
    length = int(length) # 숫자 변환을 해줘야 함!!!
    
    if length<0:
        return render(request,'password/error1.html') # 음수 입력
    
    if not (upper or lower or digits or special):
        return render(request, 'password/error3.html')  # 체크박스 아무것도 선택X
    
    # 체크박스 선택에 따른 문자 집합(set) 구성
    check_chars=''
    if upper:
        check_chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
    if lower:
        check_chars += "abcdefghijklmnopqrstuvwxyz"
        
    if digits:
        check_chars += "0123456789"
        
    if special:
        check_chars += "!@#$%^&*"
    
    # 비밀번호 생성
    generated_password = ""
    for i in range(length):
        generated_password += random.choice(check_chars)

    
    return render(request, 'password/result.html',{'password':generated_password})