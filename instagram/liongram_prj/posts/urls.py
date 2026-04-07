from django.urls import path
from .views import *

app_name = 'posts'

urlpatterns = [
    path('', list, name='list'),
    path('detail/<int:id>/', detail, name='detail'),
    path('create/', create, name='create'),
    path('update/<int:id>/', update, name='update'),
    path('delate/<int:id>/', delete, name='delete'),
    path('result', result, name='result'),
]