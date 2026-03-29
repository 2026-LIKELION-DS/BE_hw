from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def word_count(request):
    return render(request, 'word_count.html')

def result(request):
    entered_text = request.GET['fulltext']  # 요청이 들어오면 fulltext를 가져와라
    word_list = entered_text.split()    # entered_text를 공백 기준으로 문자열을 나누겠다
    
    word_dictionary = {}
    
    for word in word_list:      # {word:출현 횟수}로 만들어줌
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
    
    
    # 가장 많이 입력된 단어
    max_count = 0
    most_frequent = []
    
    if word_dictionary:
        max_count = max(word_dictionary.values())
        most_frequent = [word for word, count in word_dictionary.items() if count == max_count]

    
    
    # 글자 수 세기 (띄어쓰기 포함)
    total_len = len(entered_text)
    
    # 글자 수 (띄어쓰기 제외)
    only_letter = len(entered_text.replace(' ',''))
    
    
    
    
    return render(request, 'result.html',{
        'alltext': entered_text, 
        'dictionary':word_dictionary.items(),
        'word_count':len(word_list),
        'max_count':max_count,
        'most_frequent':most_frequent,
        'total_len':total_len,
        'only_letter':only_letter,
        
        })   # result.html에 변수 전달하기

def hello(request):
    name = request.GET['name'] # index에서 입력한 이름 받기
    return render(request, 'hello.html',{'name':name})