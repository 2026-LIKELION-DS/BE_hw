from django.urls import path
from .views import detail, update, delete, comment, comment_delete

app_name = 'everytime'

urlpatterns = [
    path('detail/<int:id>/', detail, name='detail'),
    path('update/<int:id>/', update, name='update'),
    path('delete/<int:id>/', delete, name='delete'),
    path('comment/<int:comment_id>/', comment, name='comment'),
    path('comment/delete/<int:post_id>/', comment_delete, name='comment_delete'),
]