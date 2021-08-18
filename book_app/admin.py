from django.contrib import admin
from . models import Author, Book, Review

# Register your models here.
admin.site.register(Book)
admin.site.register(Review)
admin.site.register(Author)
