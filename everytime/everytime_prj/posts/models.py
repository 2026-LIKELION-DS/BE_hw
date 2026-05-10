from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    is_anonymous = models.BooleanField(default=False)
    author = models.CharField(max_length=20)
    category = models.ManyToManyField(to=Category, through="PostCategory", related_name="posts")
    image = models.ImageField(upload_to='posts/images', null = True, blank=True )
    video = models.FileField(upload_to='posts/video', null=True, blank=True)
    like = models.ManyToManyField(to=User, through="Like", related_name="like_posts")
    scrap = models.ManyToManyField(to=User, through="Scrap", related_name="scrap_posts")
    

    def __str__(self):
        return self.title
    
class Like(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="user_likes")
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name="post_likes")

class Scrap(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="user_scraps")
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name="post_scraps")
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    is_anonymous = models.BooleanField(default=False)
    author = models.CharField(max_length=20) 

class PostCategory(models.Model):
    posts = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name="posts_categories")
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name="post_categories")