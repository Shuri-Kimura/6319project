from typing import Text
from django.shortcuts import render, get_object_or_404, redirect
from django.db import models
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic.list import ListView
from django.views import generic
from django.shortcuts import render
from users.models import Users
from .forms import TcomForm
from users.models import Tfavos,Cfavos,Classes,Texts,Tcom


class TextpageView(generic.DetailView):
    template_name = 'textpage/textpage.html'
    fields = '__all__'
    model = Texts
    
    def get_context_data(self, **kwargs):
        context = super(TextpageView, self).get_context_data(**kwargs)
        context.update({
            'tcom_list': Tcom.objects.order_by('date').reverse().all(),
            
        })
        return context

    
    def get_initial(self):
        initial = super().get_initial()
        initial["text_id"] = 1
        initial["user_id"] = self.request.user
        return initial

class AddCom(generic.CreateView):
    fields = '__all__'
    model = Tcom
    template_name = 'textpage/add_comments.html'  
    def get_initial(self):
        tcomf = TcomForm(self.request.POST, self.request.FILES)
        initial = super().get_initial()
        initial["text_id"] = Texts.objects.get(text_id = tcomf)
        initial["user_id"] = self.request.user
        return initial







  



        



      













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
