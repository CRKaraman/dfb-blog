from django.db import models
from django.urls import reverse # new

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200, default='New message')
    author = models.ForeignKey(
    'auth.User',
    on_delete=models.CASCADE, null=True
    )
    body = models.TextField(default='SOME STRING')
    
    def __str__(self):
        return self.title[:50]
    
    def get_absolute_url(self): # new
        return reverse('post_detail', args=[str(self.id)])