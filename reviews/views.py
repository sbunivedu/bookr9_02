from django.shortcuts import render
import logging

logger = logging.getLogger('django')

def index(request):
    logger.info("Hello from reviews.view!")
    return render(request, "base.html")

# views.py (or any other module)