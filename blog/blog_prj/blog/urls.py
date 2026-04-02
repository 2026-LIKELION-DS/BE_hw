from django.urls import path
from .views import list, create, detail, update, delate

app_name = 'blog'

urlpatterns = [
    path('', list, name='list'),
    path('create/', create, name='create'),
    path('detail/<int:id>/', detail, name='detail'), # 아이디 값이 경로에서 보임
    path('update/<int:id>/', update, name='update'),
    path('delete/<int:id>/', delate, name='delete'),
]