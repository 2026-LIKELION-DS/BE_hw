from django.urls import path
from .views import IndexView
from .views import result,create,detail,update,delete


app_name = 'phone'

urlpatterns = [
    path('', IndexView.as_view(), name='list'),
    path('result/', result, name='result'),
    path('create/', create, name='create'),
    path('delete/<int:id>/', delete, name='delete'),
    path('detail/<int:id>/', detail, name='detail'),
    path('update/<int:id>/', update, name='update'),
]