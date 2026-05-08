from django.urls import path
from .views import *

## 네임스페이스
app_name = "accounts"

urlpatterns = [
    
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('', mypage, name='mypage'),
    path('user-info/', user_info, name='user-info'),
    path('myblog/', myblog, name = 'myblog'),
    path('mylike/', mylike, name='mylike'),

]
