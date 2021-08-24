
from book_app.forms import ReviewForm
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, Http404
from . models import Book, Review
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage

import json

# NOTE: Reading book.json
# books_data = open(
#     'G:/Training/Shijo_playground/2021/Django/Django_CRUD/books.json').read()

# data = json.loads(books_data)


# Create your views here.

class BookListView(LoginRequiredMixin, ListView):
    template_name = "books/bookdata.html"
    context_object_name = "books"

    def get_queryset(self):
        return Book.objects.all()


class BookDetailView(DetailView):
    model = Book
    template_name = "books/showbook.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # reviews = Review.objects.filter(book_id=id).order_by('-id') -> below
        context["reviews"] = context['book'].review_set.order_by('-id')
        context["authors"] = context['book'].authors.all()
        # NOTE: intitally we created html froms to use review, now we are replacing it with django forms [showbook.html]
        context["forms"] = ReviewForm()
        return context


@login_required
def index(request):
    # NOTE: will use here HTML file as response
    current_user = request.user.username
    context = {'user':  current_user.upper(), 'appName': 'Books Store'}
    return render(request, 'books/index.html', context)


# def book_list(request):
#     # NOTE: reading data from DB
#     data = Book.objects.all()
#     context = {'books': data}
#     return render(request, 'books/bookdata.html', context)

#     # NOTE: this above code we are making more django type using genric forms, its defined in class BookListView


# def show_book(request, id):
#     '''
#     NOTE: below logic when we read from JSON
#     single_book = list()
#     for book in data:
#         if book["id"] == id:
#             single_book = book

#     context = {'book': single_book}
#     return render(request, 'books/showbook.html', context)
#     '''

#     # NOTE: reading data from DB
#     # single_book = Book.objects.filter(id=id).first() => if 'id' not available still we get empty page but using 'get' we get doesnotexist
#     '''
#     NOTE
#     Entire code below is used via get_object_or_404

#     try:
#         single_book = Book.objects.get(pk=id)
#         context = {'book': single_book}
#         return render(request, 'books/showbook.html', context)
#     except Book.DoesNotExist:
#         raise Http404(f'Book Not Found for id {id}')

#     '''

#     single_book = get_object_or_404(Book, pk=id)
#     # NOTE [latest]: orderby(id)-> ascending order ; orderby(-id)-> descending order
#     reviews = Review.objects.filter(book_id=id).order_by('-id')
#     context = {'book': single_book, 'reviews': reviews}
#     return render(request, 'books/showbook.html', context)
#     # NOTE: this above code we are making more django type using genric forms, its defined in class BookDetailView


def review(request, id):

    review_data = request.POST['body']
    newReview = Review(body=review_data, book_id=id,
                       user=request.user)

    if len(request.FILES) != 0:
        image = request.FILES['image']
        fs = FileSystemStorage()
        name = fs.save(image.name, image)
        newReview.image = fs.url(name)

    newReview.save()
    return redirect('/book/bookslist')


@login_required
def author(request, author):
    books = Book.objects.filter(authors__name=author)
    context = {'books': books}
    return render(request, 'books/bookdata.html', context)


@login_required
def cool(request):
    # NOTE: showing a basic response without html
    return HttpResponse('Cool Dude')
