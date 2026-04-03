from django.urls import path
from .views import result, create, delete, detail, update, phone_list


app_name = 'phone'

urlpatterns = [
    path('', phone_list, name='phone_list'),
    path('result/', result, name='result'),
    path('create/', create, name='create'),
    path('delete/<int:id>', delete, name='delete'),
    path('detail/<int:id>', detail, name='detail'),
    path('update/<int:id>', update, name='update'),
]
