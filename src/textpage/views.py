from django.http import HttpResponse,HttpResponseRedirect
from django.views import generic
from django.shortcuts import render
from django.utils import timezone
from users.models import Tfavos , Cfavos,Classes,Texts

#class TextpageView(ListView):
 #   template_name = 'textpage/textpage_list.html'
  #  model = Texts



class TextpageView(generic.DetailView):
    model = Texts
    template_name = 'textpage/textpage_list.html'




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
