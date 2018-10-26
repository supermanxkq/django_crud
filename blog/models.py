from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=32, default='Title')
    content = models.TextField(null=True)

    # 3.6 使用str #2.7 使用unicode
    def __str__(self):
        return self.title
