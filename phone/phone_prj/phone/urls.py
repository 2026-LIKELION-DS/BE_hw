from django.urls import path
from .views import list, search_result, create, detail, update, delete

app_name = 'phone'

urlpatterns = [
    path('', list, name = 'list'),
    path('results/', search_result, name = 'search_result'),
    path('create/', create, name = 'create'),
    path('detail/<int:id>', detail, name = 'detail'),
    path('update/<int:id>', update, name = 'update'),
    path('delete/<int:id>', delete, name = 'delete'),
]