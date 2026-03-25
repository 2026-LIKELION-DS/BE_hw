from django.shortcuts import render
from collections import Counter


def index(request):
    return render(request, 'index.html')


def word_count(request):
    return render(request, 'word_count.html')


def hello(request):
    name = request.GET.get('name', '') 
    return render(request, 'hello.html', {'name': name})


def result(request):
    entered_text = request.GET.get('fulltext', '').strip()  

    words = entered_text.split()
    total = len(words)

    word_count_dict = Counter(words)
    max_count = max(word_count_dict.values()) if word_count_dict else 0  

    most_common_words = [
        word for word, count in word_count_dict.items()
        if count == max_count
    ]

    total_len = len(entered_text)
    no_space_len = len(entered_text.replace(" ", ""))

    return render(request, 'result.html', {
        'alltext': entered_text,
        'total': total,
        'most_common_words': most_common_words,
        'total_len': total_len,
        'no_space_len': no_space_len,
        'max_count': max_count,
    })