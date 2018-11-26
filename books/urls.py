from django.urls import path
from books import views


urlpatterns = [
    # main page
    path('', views.index, name='home'),

    # testing for category pages
    path(
        'category/<slug>/',
        views.category_detail,
        name='category_detail'
    ),
]
