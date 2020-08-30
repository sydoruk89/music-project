from django.db import models
from django.urls import reverse

from django.db import models

class Music(models.Model):
    title = models.CharField(max_length=64, null=True)
    author = models.CharField(max_length=100, null=True)
    genre = models.CharField(max_length=64, null=True)
    artist = models.ForeignKey('auth.user', on_delete=models.CASCADE, null=True)
    body = models.TextField(null=True)
    time = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.author
    
    def get_absolute_url(self): 
        return reverse('home')