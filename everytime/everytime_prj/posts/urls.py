from django.urls import path
from .views import detail, update, delete, comment, comment_delete, like, scrap
from . import views

app_name = 'posts'


urlpatterns = [
    path('detail/<int:id>/', detail, name='detail'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', delete, name='delete'),
    path('comment/<int:comment_id>/', comment, name='comment'),
    path('comment/delete/<int:post_id>/', comment_delete, name='comment_delete'),
    path('', views.main, name='main'),
    path('category/<str:slug>/', views.category_detail, name='category_detail'),
    path('like/<int:post_id>/', like, name="like"),
    path('scrap/<int:post_id>/', scrap, name="scrap")
    
]