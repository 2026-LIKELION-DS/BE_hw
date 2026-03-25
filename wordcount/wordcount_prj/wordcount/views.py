from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def word_count(request):
    return render(request, 'word_count.html')

def hello(request):
    return render(request, 'hello.html')

def result(request):
    entered_text = request.GET['fulltext']
    word_list = entered_text.split()
#    name = request.GET.get['name']

    word_dictionary = {}

    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    space = len(entered_text)
    no_space = len(entered_text.replace(' ', ''))

    if word_dictionary:
        frequency = max(word_dictionary.values())
        many_word = max(word_dictionary, key = word_dictionary.get)
        many_word = [word for word, count in word_dictionary.items() if count == frequency]
    else:
        many_word = '없음'

    return render(request, 'result.html', {'alltext': entered_text, 'dictionary':word_dictionary.items(), 'no_space' : no_space, 'space' : space, 'many_word': many_word, 'frequency' : frequency, })

def hello(request):
    name = request.GET.get('my_name')
    
    return render(request, 'hello.html', {'my_name': name})