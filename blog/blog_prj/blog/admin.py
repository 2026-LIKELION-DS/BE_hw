from django.contrib import admin
from .models import *

admin.site.register(Post) #admin 사이트에서 Post 모델에 접근 가능
admin.site.register(Comment)
admin.site.register(Category)