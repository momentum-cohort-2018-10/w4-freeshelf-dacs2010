# call this class to make a subclass from it
from django.core.management.base import BaseCommand
# still working out what this does
from django.conf import settings
# get access to pathnames
import os.path
# manipulate csv files
import csv
# grab book model
from books.models import Book
# create my own file
from django.core.files import File


def get_path(file):
    # look at the base dir and get book_data and the file
    return os.path.join(settings.BASE_DIR, 'books/book_data', file)


class Command(BaseCommand):
    help = "Loads the books into the database"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        # method to delete anything if it's already there
        print("deleted books")
        Book.objects.all().delete()

        # open file as 'file'
        with open(get_path('books.csv'), 'r') as file:
            # manipulate the csv file with DictReader
            reader = csv.DictReader(file)

            # do something with each row
            for row in reader:
                # make a instance of book, and set each column accordingly
                book = Book(
                    title=row['title'],
                    author=row['author'],
                    description=row['description'],
                    book_URL=row['url'],
                )
                book.save()
        print("books are loaded")
