from django.urls import path
from .views import list, create, result
#from .views import * :path가 덮어쓰여질 수 있음 -> 명시적으로 import!
#from . import views : views.list, views.create, views.result로 작성

app_name = "phone"

urlpatterns = [
    path("", list, name="list"),
    path("create/", create, name="create"),
    path("result/", result, name="result"),
]
