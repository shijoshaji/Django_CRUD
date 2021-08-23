from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.contrib.auth.models import User

# Create your models here.


class Author(models.Model):
    name = models.CharField(verbose_name='Author Full name', max_length=50)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    pageCount = models.IntegerField(default=0)
    thumbnailUrl = models.CharField(max_length=200, null=True)
    shortDescription = models.CharField(max_length=100, null=True)
    longDescription = models.TextField(max_length=500, null=True)
    status = models.CharField(max_length=50, null=True)
    isbn = models.IntegerField(default=9999)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.title


class Review(models.Model):
    body = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # book_id = models.BigIntegerField(default=1) -> below relationship we created
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.body
