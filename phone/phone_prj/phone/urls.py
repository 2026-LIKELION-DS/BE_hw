from django.urls import path
from .views import list, search_result, create, detail, update, delete, IndexView

app_name = 'phone'

urlpatterns = [
    path('', IndexView.as_view(), name='list'),
    path('results/', IndexView.as_view(), name='search_result'),
    path('create/', create, name = 'create'),
    path('detail/<int:id>', detail, name = 'detail'),
    path('update/<int:id>', update, name = 'update'),
    path('delete/<int:id>', delete, name = 'delete'),
]

