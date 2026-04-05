from django.urls import path
from .views import result, create, delete, detail, update, PhoneListView


app_name = 'phone'

urlpatterns = [
    path('', PhoneListView.as_view(), name='phone_list'),
    path('result/', result, name='result'),
    path('create/', create, name='create'),
    path('delete/<int:id>', delete, name='delete'),
    path('detail/<int:id>', detail, name='detail'),
    path('update/<int:id>', update, name='update'),
]
