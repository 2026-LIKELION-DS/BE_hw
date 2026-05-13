from django.urls import path
from .views import main, delete, comment_delete, update, detail, category, like, scrap

app_name = 'posts'

urlpatterns = [
    path("", main, name='main'),
    path("comment_delete/<int:comment_id>/", comment_delete, name='comment_delete'),
    path("delete/<int:post_id>/", delete, name='delete'),   
    path("update/<int:post_id>/", update, name='update'),
    path("detail/<int:post_id>/", detail, name='detail'),
    path("category/<slug:slug>/", category, name='category'),
    path("like/<int:post_id>/", like, name='like'),
    path("scrap/<int:post_id>/", scrap, name='scrap'),
]
