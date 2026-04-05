from django.urls import path
from  .views import list, create, detail, update
from  . import views

app_name = 'posts'

urlpatterns =[
    path('', list, name = 'list'),
    path('create/', create, name = 'create'),
    path('detail/<int:id>/', detail, name = 'detail'),
    path('update/<int:id>/', update, name = 'update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('search/', views.search, name='result'),
]