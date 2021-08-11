from django.db import models
from django.db.models.fields import CharField

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=100)
    pageCount = models.IntegerField(default=0)
    thumbnailUrl = models.CharField(max_length=200, null=True)
    shortDescription = models.CharField(max_length=100, null=True)
    longDescription = models.TextField(max_length=500, null=True)
    status = models.CharField(max_length=50, null=True)
    isbn = models.IntegerField(default=9999)

    def __str__(self):
        return self.title


class Review(models.Model):
    body = models.TextField(max_length=500)
    book_id = models.BigIntegerField(default=1)

    def __str__(self):
        return self.body
