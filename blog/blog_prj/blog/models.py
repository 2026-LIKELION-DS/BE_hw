from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 50) #50자 제한
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True) #객체 생성 시간 자동 저장

    def __str__(self):
        return self.title