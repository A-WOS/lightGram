from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    """
    라이트그램의 글 작성 부분
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    photo = models.ImageField(upload_to="photo")


class Answer(models.Model):
    """
    Post에 달릴 댓글들
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

