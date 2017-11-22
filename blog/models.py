from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Blog(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=200)
    authors_name = models.CharField(max_length=50)
    content = models.TextField()
    posted_date=models.DateTimeField('date published')
    
class Comment(models.Model):
    def __str__(self):
        return self.content
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50)
    email = models.EmailField
    content = models.TextField()
    posted_date=models.DateTimeField('date published')