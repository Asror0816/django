from books import views
from django.urls import path

urlpatterns = [
    path('index/', views.index, name='index'),
    path('books/', views.books, name='books'),
    path('contact/', views.contact, name='contact'),
]