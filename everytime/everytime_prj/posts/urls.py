from django.urls import path
from .views import main

app_name = 'posts'

urlpatterns = [
    path("", main, name='main'),
]

