from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.


class Category(models.Model):
    '''
    category
    '''
    subject = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.subject

class Book(models.Model):
    '''
    Book class
    '''
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    book_URL = models.URLField(max_length=200)
    slug = models.SlugField(unique=True)
    date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def save(self):
        if not self.id:
            self.slug = slugify(self.title)
        super(Book, self).save()
