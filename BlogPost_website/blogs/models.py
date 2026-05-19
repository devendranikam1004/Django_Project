from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

now = datetime.now()
time = now.strftime("%d %B %Y")

class Post(models.Model):
    postname = models.CharField(max_length=600)
    category = models.CharField(max_length=200)
    image = models.ImageField(upload_to='image/posts', blank=True, null=True)
    content = models.TextField()
    time = models.CharField(default=time, max_length=100, blank=True)
    likes = models.IntegerField(default=0, blank=True, null= True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.postname

class Comment(models.Model):
    content = models.TextField()
    time = models.CharField(default= time, max_length=100, blank=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.id}.{self.content[:20]}..."
    
class Contact(models.Model):
    name = models.CharField(max_length=600)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=200)
    message = models.TextField(blank=True)
    
    def __str__(self):
        return self.name