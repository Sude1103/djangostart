from django.contrib import admin

from books.models import Book, BookType


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__', 'isbn', 'page_count')


class BookTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(BookType, BookTypeAdmin)
