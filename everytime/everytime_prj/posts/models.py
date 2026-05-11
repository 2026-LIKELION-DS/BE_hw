from django.db import models
from django.conf import settings
import os
from uuid import uuid4
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length= 50, unique = True)
    slug = models.SlugField(max_length = 50, unique = True, blank = True, null = True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_anonymous = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True )
    updated_at = models.DateTimeField(auto_now = True)
    category = models.ManyToManyField(to = Category, through = "PostCategory", related_name= "posts")
    image = models.ImageField(upload_to='upload_filepath', blank=True)
    video = models.FileField(upload_to='upload_filepath', blank=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_posts', blank=True)
    scraps = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='scrapped_posts', blank=True) 

class Comment(models.Model):
    post = models.ForeignKey(to = Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    is_anonymous = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class PostCategory(models.Model):
    post = models.ForeignKey(to = Post, on_delete= models.CASCADE, related_name = "post_categories")
    category = models.ForeignKey(to = Category, on_delete = models.CASCADE, related_name="post_categories")
   
def upload_filepath(instance,filename):
    today_str=timezone.now().strftime("%Y%m%d")
    file_basename=os.path.basename(filename)
    return f'{instance._meta.model_name}/{today_str}/{str(uuid4())}_{file_basename}'