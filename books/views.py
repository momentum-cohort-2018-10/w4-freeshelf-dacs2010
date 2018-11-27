from django.shortcuts import render
from books.models import Book, Category



# Create your views here.
def index(request):
    '''
    render index.html
    '''
    categorys = Category.objects.all()
    books = Book.objects.all().order_by('-date')
    return render(request, 'books/index.html', {
        'books': books,
        'categorys': categorys,
    })


def category_detail(request, slug):
    '''
    category pages
    '''
    category = Category.objects.get(slug=slug)
    books = Book.objects.filter(category=category)
    return render(request, 'categorys/category_detail.html', {
        'books': books,
        'category': category,
    })
