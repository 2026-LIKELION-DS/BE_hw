from django.db import models
from users.models import User
import os
from uuid import uuid4
from django.utils import timezone

def upload_filepath(instance, filename):
    today_str = timezone.now().strftime("%Y%m%d")
    file_basename = os.path.basename(filename)
    return f'{instance._meta.model_name}/{today_str}/{str(uuid4())}_{file_basename}'


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    is_anonymous = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='posts')
    category = models.ManyToManyField(to='Category', related_name='posts', through='PostCategory')
    image = models.ImageField(upload_to=upload_filepath, blank=True, null=True)
    video = models.FileField(upload_to=upload_filepath, blank=True, null=True)
    like = models.ManyToManyField(to=User, related_name='liked_posts', through='Like')
    scrap = models.ManyToManyField(to=User, related_name='scraped_posts', through='Scrap')
    

    def __str__(self):
        return f'[{self.id}] {self.title}'

class Comment(models.Model):
    post = models.ForeignKey(to=Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_anonymous = models.BooleanField(default=False)

    def __str__(self):
        return f'[{self.id}] {self.content}'

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True, null=True)
    
    def __str__(self):
        return f'{self.name}'

class PostCategory(models.Model):
    post = models.ForeignKey(to=Post, related_name='post_categories', on_delete=models.CASCADE)
    category = models.ForeignKey(to=Category, related_name='category_posts', on_delete=models.CASCADE)
    
class Like(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='likes')

class Scrap(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='scraps')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='scraps')
