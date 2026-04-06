from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    # 조회수 증가 반영되는 함수
    def update_views(self):  
        self.views += 1
        self.save()






# from django.db import models

# # Create your models here.
# class Post(models.Model):
#     title = models.CharField(max_length=50)
#     content = models.TextField()
#     created_at = models.DateField(auto_now_add = True) 
    
#     def __str__(self):
#         return self.title