from django.shortcuts import render
from django.http import HttpResponse

import json

# NOTE: Reading book.json
books_data = open(
    'G:/Training/Shijo_playground/2021/Django/Django_CRUD/books.json').read()

data = json.loads(books_data)

# Create your views here.


def index(request):
    # NOTE: will use here HTML file as response
    context = {'user': 'Shijo Shaji', 'appName': 'Books Store'}
    return render(request, 'books/index.html', context)


def book_list(request):
    context = {'books': data}
    return render(request, 'books/bookdata.html', context)


def cool(request):
    # NOTE: showing a basic response without html
    return HttpResponse('Cool Dude')
