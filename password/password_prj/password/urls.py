from django.urls import path
from . import views
from .views import *

app_name = 'password'

urlpatterns = [
    path('', views.index, name='index'),
    path('result/', views.password_generator, name='result'),
    path('error1/', error1, name='error1'), 
    path('error2/', error2, name='error2'),
    path('error3/', error3, name='error3'),
]