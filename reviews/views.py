from django.shortcuts import render
import logging

logger = logging.getLogger('django')

def index(request):
    logger.info("Hello from reviews.view!")
    name = "world"
    return render(request, "base.html", {"name": name})

# views.py (or any other module)