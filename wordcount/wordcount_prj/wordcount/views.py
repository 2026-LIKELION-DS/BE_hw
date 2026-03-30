from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def word_count(request):
    return render(request, 'word_count.html')

def result(request):
    entered_text = request.GET['fulltext']
    word_list = entered_text.split()
    total_count = len(word_list)
    full_length = len(entered_text)
    no_space_length = len(entered_text.replace(" ", ""))
    
    word_dictionary = {}

    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
    
    max_count = 0
    most_frequent_words = []

    if word_dictionary:
        max_count = max(word_dictionary.values())
        
        for word, count in word_dictionary.items():
            if count == max_count:
                most_frequent_words.append(word)

    return render(request, 'result.html', {'alltext': entered_text, 'dictionary': word_dictionary.items(), 'total': total_count, 'most_word':most_frequent_words, 'max_c': max_count, 'full_len': full_length, 'no_space_len': no_space_length,})

def hello(request):
    entered_name = request.GET.get('user_name')
    return render(request, 'hello.html', {'name': entered_name})
