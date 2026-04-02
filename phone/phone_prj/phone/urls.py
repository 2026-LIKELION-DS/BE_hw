from django.urls import path
from .views import *

app_name = 'phone'

urlpatterns = [
    path('', list, name='list'),
    path('create/', create, name='create'),
    path('detail/<int:id>/', detail, name='detail'),
    path('result/', result, name='result'),
]