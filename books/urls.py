from django.urls import path
from books import views


urlpatterns = [
    # main page
    path('', views.index, name='home'),
    path('things/<slug>/',
         views.category_detail,
         name='category_detail'
    ),
]
