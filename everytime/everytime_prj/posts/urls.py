from django.urls import path
from .views import main, delete, comment_delete, update, detail

app_name = 'posts'

urlpatterns = [
    path("", main, name='main'),
    path("comment_delete/<int:comment_id>/", comment_delete, name='comment_delete'),
    path("delete/<int:post_id>/", delete, name='delete'),   
    path("update/<int:post_id>/", update, name='update'),
    path("detail/<int:post_id>/", detail, name='detail'),
]

