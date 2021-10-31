from django.http import HttpResponse
from django.template import loader

from users.models import Cfavos , Tfavos

def index(request):
    return HttpResponse("Hello, world. 6319project.like")