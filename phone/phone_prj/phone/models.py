from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=10)
    number = models.CharField(max_length=11)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.number:
            self.number = self.number.replace("-", "")

        super().save(*args, **kwargs)
