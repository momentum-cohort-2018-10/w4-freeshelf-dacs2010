from django.urls import path
from books import views


urlpatterns = [
    # main page
    path('', views.index, name='home'),

    # testing for book pages
    path(
        'books/<slug>/',
        views.book_detail,
        name='book_detail'
    ),
]
