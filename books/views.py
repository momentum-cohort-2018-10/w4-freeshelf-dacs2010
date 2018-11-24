from django.shortcuts import render
from books.models import Book, Category


# Create your views here.
def index(request):
    '''
    render index.html
    '''
    books = Book.objects.all()
    return render(request, 'books/index.html', {
        'books': books
    })

def category_detail(request, slug):
    '''
    individual pages for each category
    '''
    category = Category.objects.get(slug=slug)
    return render(request, 'things/thing_detil.html', {
        'category': category,
    })
