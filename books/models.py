from django.db import models


class BookType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    book_name = models.CharField(max_length=50)
    isbn = models.PositiveBigIntegerField(null=True, blank=True)
    book_type = models.ForeignKey(BookType, on_delete=models.PROTECT, null=True, blank=True)
    page_count = models.PositiveSmallIntegerField(null=True, blank=True)
    descriptions = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f'{self.book_name}({self.isbn})'
