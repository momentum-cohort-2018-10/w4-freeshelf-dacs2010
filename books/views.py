from django.shortcuts import render
from books.models import Book, Category


# Create your views here.
def index(request):
    '''
    render index.html
    '''
    categorys = Category.objects.all()
    books = Book.objects.all()
    return render(request, 'books/index.html', {
        'books': books,
        'categorys': categorys,
    })


def book_detail(request, slug):
    '''
    book details pages
    '''
    book = Book.object.get(slug=slug)
    return render(request, 'books/book_detail.html', {
        'book': book,
    })
