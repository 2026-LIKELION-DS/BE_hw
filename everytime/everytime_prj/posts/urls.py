from django.urls import path
from everytime import views as everytime_views 

app_name = 'posts'

urlpatterns = [
    path('', everytime_views.main, name='main'), 
]