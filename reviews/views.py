from django.http import HttpResponse
import logging

logger = logging.getLogger('django')

def index(request):
    logger.info("Hello from my_view!")
    name = request.GET.get("name") or "world"
    return HttpResponse("Hello, {}!".format(name))

# views.py (or any other module)