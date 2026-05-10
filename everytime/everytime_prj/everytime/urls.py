from django.urls import path
from . import views

app_name = 'everytime'

urlpatterns = [
    path('', views.main, name='main'), 
    path('category/<slug:slug>/', views.category, name='category'),
]