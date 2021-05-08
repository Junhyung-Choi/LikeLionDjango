from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    writer = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()

class Visitor(models.Model):
    visitor_id = models.CharField(max_length=100)
    visitor_password = models.CharField(max_length=100)
    visitor_signupdate = models.DateField()