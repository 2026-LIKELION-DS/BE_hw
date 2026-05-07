from django.urls import path
from  .views import *

app_name = 'accounts'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('', mypage, name='mypage'),
    path('user-info/', user_info, name='user-info'),
    path('myblog/', myblog, name='myblog'), #주소로 접속하면 myblog 함수 실행
    path('mylike/', mylike, name='mylike'),
]