from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    writer = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()

class Teammate(models.Model):
    fullname = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    birthday = models.DateField()
    nickname = models.CharField(max_length=100)
    mbti = models.CharField(max_length=4)
    hobby = models.CharField(max_length=100)
    favorfood = models.CharField(max_length=100)