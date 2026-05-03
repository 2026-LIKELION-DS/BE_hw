from django.urls import path
from  .views import *

app_name = 'posts'

urlpatterns = [
    path('', main, name = 'main'),
    path('create/', create, name = 'create'), 
    path('detail/<int:id>/', detail, name='detail'),
    path('update/<int:id>/', update, name='update'),
    path('delete/<int:id>/', delete, name='delete'),
    path('create-comment/<int:post_id>/', create_comment, name='create-comment'),
    path('comment-delete/<int:id>/', comment_delete, name='comment_delete')
]