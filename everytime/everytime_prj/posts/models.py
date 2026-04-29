from django.db import models
from users.models import User
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TestField()
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="posts")
    is_anonymouse = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.id}] self.title'