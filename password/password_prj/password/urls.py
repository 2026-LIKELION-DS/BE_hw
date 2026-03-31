from django.urls import path
from .views import *

app_name = 'password'

urlpatterns = [
    path('',index, name='index'),
    path('password-generator/', password_generator, name='password_generator'),
]
