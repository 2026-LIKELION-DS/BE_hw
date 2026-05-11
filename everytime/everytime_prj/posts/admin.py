from django.contrib import admin
from posts.models import Post, Category, PostCategory, Comment

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(PostCategory)
admin.site.register(Comment)
