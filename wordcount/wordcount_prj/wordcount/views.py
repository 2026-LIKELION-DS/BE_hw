from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def word_count(request):
    return render(request, 'word_count.html')

def result(request):
    entered_text = request.GET['fulltext']
    word_list = entered_text.split()

    word_dictionary = {}
    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word]+=1
        else:
            word_dictionary[word]=1

    word_count = len(word_list)

    max_count = 0
    max_words = []

    for word, count in word_dictionary.items():
        if count > max_count:
            max_count = count
            max_words = [word]
        elif count == max_count:
            max_words.append(word)

    total_length = len(entered_text)
    no_space_length = len(entered_text.replace(" ", ""))

    return render(request, 'result.html', {
        'alltext': entered_text,
        'dictionary': word_dictionary.items(),
        'word_count': word_count,
        'max_words': max_words,
        'max_count': max_count,
        'total_length': total_length,
        'no_space_length': no_space_length
    })


def hello(request):
    name = request.GET['name']
    return render(request, 'hello.html', {'name': name})