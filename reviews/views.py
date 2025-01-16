from django.http import HttpResponse
import logging

logger = logging.getLogger('django')

def index(request):
    logger.info("Hello from my_view!")
    return HttpResponse("Hello, world!")

# views.py (or any other module)