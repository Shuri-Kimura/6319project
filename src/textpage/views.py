#from django.http import HttpResponse
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"


#def index(request):
    
    #return HttpResponse("Hello, world. 6319project.textpage")
# Create your views here.
