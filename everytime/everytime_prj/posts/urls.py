# posts/urls.py
from django.urls import path
from .views import *

app_name = 'posts'

urlpatterns = [
    path('', main, name='main'),
    path('detail/<int:id>/', detail, name='detail'),
    path('detail/<int:id>/comment/create/', comment_create, name='comment_create'),
    path('comment/<int:com_id>/delete/', comment_delete, name='comment_delete'),
    path('detail/<int:id>/delete/', post_delete, name='delete'), 
    path('detail/<int:id>/update/', post_update, name='update'),
]