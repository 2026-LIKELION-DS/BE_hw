from django.urls import path
from .views import *
from .views import IndexView

app_name = 'phone'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create/', create, name='create'),
    path('detail/<int:id>/', detail, name='detail'),
    path('result/', result, name='result'),
    path('update/<int:id>/', update, name='update'),
    path('delete/<int:id>/', delete, name='delete'),
]