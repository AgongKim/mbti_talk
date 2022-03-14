from importlib.resources import contents
from pyexpat import model
from unicodedata import category
from django.db import models
from user.models import User
from mbti_talk.configs import BOARD_CATEGORIES

# Create your models here.
class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    category = models.CharField(max_length=100,choices=BOARD_CATEGORIES)
    title = models.CharField(max_length=1000)
    contents = models.TextField()
    hits = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'app_article'
        app_label = 'article'
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.full_clean()
        super(User, self).save(*args, **kwargs)

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    contents = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'app_comment'
        app_label = 'article'
    
    def __str__(self):
        return self.contents

    def save(self, *args, **kwargs):
        self.full_clean()
        super(User, self).save(*args, **kwargs)

class ArticleLike(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'app_article_like'
        app_label = 'article'

