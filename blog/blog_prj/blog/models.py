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
    title = models.CharField(max_length = 50) #50자 제한
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True) #객체 생성 시간 자동 저장
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="posts") #게시글을 하나의 작성자에 연결
    image = models.ImageField(upload_to=upload_filepath, blank=True)
    video = models.FileField(upload_to=upload_filepath, blank=True)

    def __str__(self):
        return f'[{self.id}] self.title' #게시글 출력 시 ID와 제목 함께 반환
    

class Comment(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name="comments") #댓글을 하나의 post에 연결
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="comments") #댓글을 하나의 User에 연결

    def __str__(self):
        return f'[{self.id}] {self.content}' #댓글 출력 시 ID와 내용 함께 반환