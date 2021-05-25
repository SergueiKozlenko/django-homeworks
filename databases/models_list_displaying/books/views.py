from django.shortcuts import render
from django.urls import reverse

from books.models import Book


def home_view(request):
    template = 'books/books_list.html'
    context = {}
    return render(request, template, context)


def books_view(request, pub_date=None):
    template = 'books/books_list.html'
    books = Book.objects.all().order_by('-pub_date')
    books_dates = books.order_by('-pub_date').values('pub_date').distinct()

    pages = {}
    for index, date in enumerate(list(books_dates)):
        pages[index + 1] = date['pub_date']

    prev_page, next_page = {}, {}

    if pub_date:
        books = books.filter(pub_date=pub_date)
        total_pages = len(pages)
        try:
            current_page = [key for (key, value) in pages.items() if value == pub_date][0]
        except IndexError:
            current_page = 1
        if current_page < 1:
            current_page = 1
        if current_page > 1:
            prev_page = {'url': reverse('books', args=[pages[current_page - 1]]),
                         'pub_date': str(pages[current_page - 1])
                         }
        if current_page < total_pages:
            next_page = {'url': reverse('books', args=[pages[current_page + 1]]),
                         'pub_date': str(pages[current_page + 1])
                         }
    context = {'books': books,
               'prev_page': prev_page,
               'next_page': next_page
               }
    return render(request, template, context)
