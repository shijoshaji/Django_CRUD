from django.urls import path
from . import views

urlpatterns = [
    path('/', views.index, name='index'),
    path('/cool', views.cool, name='cool'),
    path('/bookslist', views.book_list, name='bookslist')
]
