from django.contrib import admin
from books.models import Book, Category


class BookAdmin(admin.ModelAdmin):
    '''
    book admin
    '''
    model = Book
    list_display = (
        'title',
        'author',
        'description',
        'date',
        'category',
    )
    prepopulated_fields = {
        'slug': ('title',)
    }


class CategoryAdmin(admin.ModelAdmin):
    '''
    category admin
    '''
    model = Category
    list_display = (
        'subject',
    )
    prepopulated_fields = {
        'slug': ('subject',)
    }


# register admin
admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)
