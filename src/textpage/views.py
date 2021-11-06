#from django.shortcuts import render
from django.views.generic import TemplateView
class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        ctext = super().get_context_data()
        ctext["textname"] = "久保耀希　取扱い説明書"
        ctext["num_love"] = 99
        ctext["num_comment"] = 99
        return ctext

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
