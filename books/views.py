from django.shortcuts import render
from books.models import Book


# Create your views here.
def index(request):
    '''
    render index.html
    '''
    return render(request, 'books/index.html')
