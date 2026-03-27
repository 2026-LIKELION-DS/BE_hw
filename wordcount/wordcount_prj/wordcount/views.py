from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html') #index 함수 실행하면 index.html 파일 보여 줌

def word_count(request):
    return render(request, 'word_count.html')

def result(request):
    entered_text = request.GET['fulltext'] # 요청이 들어오면 fulltext를 가져옴
    word_list = entered_text.split() #entered_text를 공백 기준으로 문자열 나눔

    word_dictionary = {}

    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
    
    # 과제: 가장 많이 입력된 단어
    max_word = ''
    max_count = 0

    for word, count in word_dictionary.items():
        if count > max_count:
            max_count = count
            max_word = word
    
    # 과제: 글자 수
    total_len = len(entered_text)

    # 과제: 글자 수 띄어쓰기 제외
    no_space_len = len(entered_text.replace(" ", ""))

    return render(request, 'result.html',
    {'alltext': entered_text,
    'dictionary':word_dictionary.items(),
    'count':len(word_list),
    'max_word':max_word,
    'max_count': max_count,
    'total_len':total_len,
    'no_space_len':no_space_len})

def hello(request):
    name = request.GET['name']
    return render(request, 'hello.html', {'name': name})