from django.urls import path
from .views import *

app_name = 'posts'

urlpatterns =[
    path('', main, name ='main'),
    path('detail/<int:post_id>/', detail, name = 'detail'),
    path('update/<int:post_id>/', update, name ='update'),
    path('delete/<int:post_id>/', delete, name = 'delete'),
    path('comment_delete/<int:comment_id>/', comment_delete, name = 'comment_delete'),
    path('comment_create/<int:post_id>/', comment_create, name='comment_create'),
]