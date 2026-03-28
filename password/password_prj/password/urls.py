# password/urls.py
from django.urls import path
from . import views

app_name = 'password'

urlpatterns = [
    path('', views.index, name='index'),
    path('result/', views.password_generator, name='result'),
]