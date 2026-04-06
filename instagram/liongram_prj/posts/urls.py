from django.urls import path
from .views import * # from . import views

app_name = 'posts'

urlpatterns = [
    path('', list, name='list'),
    path('create/',create,name='create'),
    path('detail/<int:id>/', detail, name='detail'),
    path('result/', result, name='result'),
    path('update/<int:id>/',update, name='update'),
    path('delete/<int:id>/',delete,name='delete'),
]
