from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    book_URL = models.URLField(max_length=200)
    slug = models.SlugField(unique=True)
    date = models.DateField(auto_now_add=True)
    
    def save(self):
        if not self.id:
            self.slug = slugify(self.title)