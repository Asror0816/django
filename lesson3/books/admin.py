from django.contrib import admin

from books.models import *
# Register your models here.

class BooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','year', 'author', 'is_active')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'author','year')

admin.site.register(Book, BooksAdmin)