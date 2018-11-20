from django.db import models
from datetime import datetime

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    URL = models.URLField(max_length=200)
    slug = models.SlugField(unique=True)
    date = models.DateField(auto_now_add=True)
