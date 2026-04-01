from django.urls import path
from .views import list, create, detail, update, result

app_name = 'phone'

urlpatterns = [
    path('', list, name = 'list'), 
    path('create/', create, name = 'create'), 
    path('update/<int:id>/', update, name='update'), 
    path('result/', result, name='result'),
]