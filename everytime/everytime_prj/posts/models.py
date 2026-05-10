from django.db import models
from users.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True, null=True)

    def __str__(self):
        return f'[{self.id}] self.content'
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="posts")
    is_anonymous = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name="posts")
    like = models.ManyToManyField(to=User, through="Like", related_name="likeed_posts")
    scrap = models.ManyToManyField(to=User, through="scrap", related_name="scraped_posts")

    def __str__(self):
        return f'[{self.id}] self.title'
    
class Comment(models.Model):
    post = models.ForeignKey(to=Post, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="comments")
    is_anonymous = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.id}] self.content'
    
class PostCategory(models.Model):
    posts = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name="post_categories")
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name="post_categories")

class Like(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name="user_likes")
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="user_likes")

class Scrap(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name="user_scraps")
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="user_scraps")
