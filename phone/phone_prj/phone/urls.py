from django.urls import path
from .views import list, search_result, create

app_name = 'phone'

urlpatterns = [
    path('', list, name = 'list'),
    path('results/', search_result, name = 'search_result'),
    path('create/', create, name = 'create'),
]