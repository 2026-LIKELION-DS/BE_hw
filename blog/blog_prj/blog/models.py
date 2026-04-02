from django.db import models

class Post(models.Model): # 상속받음
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title # 글 제목으로 admin 페이지에서 목록 확인