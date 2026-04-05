from django.urls import path
from . import views
from .views import list, create, detail, update, result, delete

app_name = 'phone'

urlpatterns = [
    path('', views.list, name = 'list'), 
    path('create/', create, name = 'create'), 
    path('update/<int:id>/', update, name='update'), 
    path('result/', result, name='result'),
    path('detail/<int:id>/', detail, name = 'detail'), 
    path('delete/<int:id>/', delete, name='delete'), 
]