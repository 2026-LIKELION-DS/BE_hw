from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def word_count(request):
    return render(request, 'word_count.html')

def hello(request):
    user_name = request.GET.get('name_input','이름')
    return render(request, 'hello.html', {'name': user_name})

def result(request):
    entered_text = request.GET['fulltext']
    word_list = entered_text.split()
    total_word_count = len(word_list)

    word_dictionary = {}
    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
    
    sorted_dictionary = sorted(word_dictionary.items(), key=lambda x: x[1], reverse=True)
    
    if sorted_dictionary:
        most_common_word = sorted_dictionary[0] # ('단어', 횟수) 형태
    else:
        most_common_word = None
    no_space_cnt = len(entered_text.replace(" ", "").replace("\n", "").replace("\r", ""))

    return render(request, 'result.html', {'alltext': entered_text, 'dictionary': sorted_dictionary,
        'total_word_count': total_word_count,
        'no_space_cnt': no_space_cnt})