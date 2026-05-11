from django.urls import path
from .views import *

app_name = 'posts'

urlpatterns = [
    path('', main, name='main'),
    path('create/<slug:slug>/',create, name='create'), # slug 추가?
    path('detail/<int:post_id>/',detail,name='detail'),
    path('delete/<int:post_id>/',delete, name='delete'),
    path('update/<int:post_id>/',update, name='update'),
    path('create-comment/<int:post_id>/',create_comment, name='create_comment'),
    path('delete-comment/<int:comment_id>/',delete_comment, name='delete_comment'),
    path('like/<int:post_id>/',like, name='like'),
    path('scrap/<int:post_id>/',scrap, name='scrap'),
    path('category/<slug:slug>/', category_list, name='category_list'),
    
]