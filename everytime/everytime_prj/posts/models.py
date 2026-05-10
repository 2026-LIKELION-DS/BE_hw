from django.db import models
from users.models import User

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True, null=True)
    
    def __str__(self):
        return self.name

    
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="posts")
    is_anonymous = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    category = models.ManyToManyField(to=Category, through="PostCategory", related_name="posts")
    likes = models.ManyToManyField(to=User, related_name="liked_posts", blank=True)
    scraps = models.ManyToManyField(to=User, related_name="scrapped_posts", blank=True)

    def __str__(self):
        return f'[{self.id}] {self.title}'
    
    class Meta:
        ordering = ['-created_at']


class Comment(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(to = User, on_delete=models.CASCADE, related_name="comments")
    is_anonymous = models.BooleanField(default = False)

    def __str__(self):
        return f'[{self.id}] {self.content}'
    


class PostCategory(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name="post_categories")
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name="post_categories")

