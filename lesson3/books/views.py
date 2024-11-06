from django.shortcuts import render
from django.http import HttpResponse

from books.models import Book


def index(request):
    return render(request, 'index.html')

def books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'books.html', context)

def contact(request):

    context = {}
    return render(request, 'contact.html', context)