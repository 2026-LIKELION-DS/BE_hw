from django.db import models
from users.models import User


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    is_anonymous = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='posts')

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
# Create your models here.