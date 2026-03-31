from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'wordcount/index.html')

def word_count(request):
    return render(request, 'wordcount/word_count.html')

def result(request):
    #요청이 들어오면 fulltext 가져오기
    entered_text = request.GET.get('fulltext')
    #entered_text 공백 기준 문자열로 나누기
    word_list = entered_text.split()
    
    #글자수
    text_len = len(entered_text)
    text_len_n = len(entered_text.replace(" ", ""))
    
    word_dictionary = {}
    
    #{word : 출현횟수}
    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
    
    max_count = max(word_dictionary.values())

    max_word = [word for word, count in word_dictionary.items() if count == max_count]
    
    word_count = len(word_dictionary)
    
    #result.html에 변수 전달
    return render(request, 'wordcount/result.html', {'alltext': entered_text, 'dictionary': word_dictionary.items(), 'text_len':text_len,
                                        'text_len_n':text_len_n,'max_word':max_word,'max_count':max_count,'word_count':word_count })

def hello(request):
    entered_text = request.GET.get('name')
    return render(request, 'wordcount/hello.html', {'name': entered_text})
