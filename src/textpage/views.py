from django.shortcuts import render
from django.http import HttpResponse
from users.models import Classes, Texts
from django.db.models import Q, Avg
from .models import SnsModel

def index(request):
    images = SnsModel.objects.all()
    context = {'images':images}
    return render(request, 'realtextpage.html', context)







#def index(request):
 # content = {
  #'message': 'こんにちは！Djangoテンプレート！'
  #}
  #return render(request, 'index.html', content)



#from django.http import HttpResponse
#from django.views.generic import TemplateView


#class IndexView(TemplateView):
    #template_name = "index.html"


#def index(request):
    
    #return HttpResponse("Hello, world. 6319project.textpage")
# Create your views here.
