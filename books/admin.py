from django.contrib import admin
from books.models import Book


class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = (
        'title',
        'author',
        'description',
        'date',
    )
    prepopulated_fields = {
        'slug': ('title',)
    }


# register admin
admin.site.register(Book, BookAdmin)
