from django.urls import path
from .views import *
from wordcount import views

app_name = 'wordcount'

urlpatterns =[
    path('', index, name='index'),
    path('word-count/',word_count, name='word_count'),
    path('result/',result, name='result'),
    path('hello/', views.hello, name = 'hello'),
]
