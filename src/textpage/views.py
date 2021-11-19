from typing import Text
from django.http import HttpResponse,HttpResponseRedirect
from django.views import generic
from django.shortcuts import render
from users.models import Users
from django.utils import timezone
from users.models import Tfavos,Cfavos,Classes,Texts,Tcom

#class TextpageView(ListView):
    #template_name = 'textpage/textpage.html'
    #model = Texts

def textpage(request):
    return textpage(request, 'textpage/textpage.html')

def get_queryset(self):
       return Tcom.objects.filter(text_id__isnull = False)

def get_queryset(self):
       return Texts.objects.filter(text_id__isnull = False)       




class TextpageView(generic.DetailView):
    model = Texts
    model2 = Tcom
    template_name = 'textpage/textpage.html'











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
