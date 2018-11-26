from django.shortcuts import render
from books.models import Book, Category


# Create your views here.
def category_detail(request, slug):
    '''
    category pages
    '''
    categorys = Category.objects.all()
    return render(request, 'categorys/category_detail.html', {
        'categorys': categorys,
    })


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
