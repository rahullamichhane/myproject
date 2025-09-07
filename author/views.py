from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Book,Author

# Create your views here.

def addAuthorsAndBooks(request):
    author1 = Author.objects.create(name="J.k Rowling",country="USA")
    author2 = Author.objects.create(name="George Orwell", country="USA")
    
    Book.objects.create(title="Harry Potter",author=author1)
    Book.objects.create(title="Animal Farm",author=author2)
    Book.objects.create(title="1984", author=author1)
    return HttpResponse("All Authors and Books are Added in Database", request)

def queryJoins(request,id):
    author = Author.objects.get(name="George Orwell")
    books_by_author = author.book_set.all()

    for book in books_by_author:
        print(book.title)

    return HttpResponse(books_by_author,request)