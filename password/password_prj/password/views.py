from django.shortcuts import render
import random

def index(request):
    return render(request, 'password/index.html')

def password_generator(request):
    # form에 입력된 정보 가져오기
    length = request.GET.get('length')

    # error2: 비밀번호 길이 입력 여부 확인
    if not length:
        return render(request, 'password/error2.html')
    
    try:
        length = int(length)
    except:
        return render(request, 'password/error2.html')

    # error1: 비밀번호가 음수값인지 확인
    if int(length) < 0:
        return render(request, 'password/error1.html')

    # error3: 체크박스 선택했는지 확인  
    upper = 'upper' in request.GET
    lower = 'lower' in request.GET
    digits = 'digits' in request.GET
    special = 'special' in request.GET

    if not (upper or lower or digits or special):
        return render(request, 'password/error3.html')

    # 체크박스 선택에 따른 문자 집합
    check_chars = ""
    if upper:
        check_chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if lower:
        check_chars += 'abcdefghijklmnopqrstuvwxyz'
    if digits:
        check_chars += '0123456789'
    if special:
        check_chars += '!@#$%^&*()'

    # 비밀번호 생성
    password = ''
    for i in range(int(length)):
        password += random.choice(check_chars)

    return render(request, 'password/result.html', {'password': password})