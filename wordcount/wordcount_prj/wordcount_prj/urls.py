from django.contrib import admin
from django.urls import path, include
from wordcount import views

urlpatterns = [
    #, 꼭 작성하기, url 오타 XX
    path("admin/", admin.site.urls),
    path('', include('wordcount.urls')),
]
