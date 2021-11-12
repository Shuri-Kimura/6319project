from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from users.models import Tfavos , Cfavos,Classes,Texts

class TextpageListView(ListView):
    template_name = 'textpage/index.html'
    model = Texts







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
