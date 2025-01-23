from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
import logging

logger = logging.getLogger('django')

def index(request):
    logger.info("Hello from reviews.view!")
    name = "world"
    return render(request, "base.html", {"name": name})

def book_search(request):
    search_text = request.GET.get("search", "")
    return render(request, "search-results.html",
    {"search_text": search_text})
# views.py (or any other module)

def welcome_view(request):
    message = f"""<html><h1>Welcome to Bookr!</h1>
    <p>{Book.objects.count()} books and
    counting!</p></html>"""
    return HttpResponse(message)