from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    """博客的类，包含了博客的名称，博文等"""
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        """返回模型的名称"""
        return self.name

class Article(models.Model):
    """博文的类，需要关联到对应的博客，还需要记录添加日期"""
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    topic = models.CharField(max_length=200)
    text = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'articals'
    
    def __str__(self) -> str:
        """返回一个表示博文简要信息的字符串"""
        return f"{self.topic[:20]} | {self.text[:50]}"