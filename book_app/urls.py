from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cool', views.cool, name='cool'),
    path('bookslist', views.book_list, name='books.all'),
    path('bookslist/<int:id>', views.show_book, name='book.show'),
    path('<int:id>/review', views.review, name='book.review')

]

'''
NOTE: the name we give in path is to call dynamically the url.
# Eg: in bookdata.html we had
# <a href="books/bookslist/{{id}}" is replaced as below
# <a href={% url 'book.show' book.id %}
'''
