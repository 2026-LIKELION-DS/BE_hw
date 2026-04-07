from django.urls import path
from .views import IndexView, create, result, detail, delete, update
#from .views import * :path가 덮어쓰여질 수 있음 -> 명시적으로 import!
#from . import views : views.list, views.create, views.result로 작성

app_name = "phone"

urlpatterns = [
    path("", IndexView.as_view(), name="list"),
    path("create/", create, name="create"),
    path("result/", result, name="result"),
    path("detail/<int:id>/",detail, name="detail"),
    path("delete/<int:id>/", delete, name="delete"),
    path("update/<int:id>/", update, name="update"),
    
]
