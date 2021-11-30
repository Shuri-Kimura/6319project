from typing import Text
from django.shortcuts import render, get_object_or_404, redirect
from django.db import models
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic.list import ListView
from django.views import generic
from django.shortcuts import render
from users.models import Users
from django.utils import timezone
from users.models import Tfavos,Cfavos,Classes,Texts,Tcom


class TextpageView(ListView):
    template_name = 'textpage/textpage.html'
    model = Texts




  

""""
class TextpageView(generic.DetailView):
    model = Texts
    def textpage(request,pk):
   
     textpage = get_object_or_404(Texts, pk=pk)
   #tcoms = Tcom.objects.filter(text_id=textpage)
     return render(request, 'textpage/textpage.html',{
          'textpage' :textpage,
          #'tcoms':tcoms,
    })
"""

        



      













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
