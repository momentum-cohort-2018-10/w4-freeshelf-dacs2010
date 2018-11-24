from django.shortcuts import render
from books.models import Book


# Create your views here.
def index(request):
    '''
    render index.html
    '''
    books = Book.objects.all()
    return render(request, 'books/index.html', {
        'books': books
    })
