from typing import TextIO
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.db import models
from django.http import HttpResponse,HttpResponseRedirect, request
from django.urls.base import reverse_lazy
from django.views.generic.list import ListView
from django.views import generic
from django.shortcuts import render
from users.models import Users
from .forms import TcomForm
from users.models import Tfavos,Cfavos,Classes,Texts,Tcom


class TextpageView(generic.DetailView):
    template_name = 'textpage/textpage.html'
    
    model = Texts
    
    def get_context_data(self, **kwargs):
        context = super(TextpageView, self).get_context_data(**kwargs)
        context.update({
            'tcom_list': Tcom.objects.order_by('date').reverse().all(),
            
        })
        return context

# class AddCom(generic.CreateView):
#     fields = '__all__'
#     model = Tcom
#     template_name = 'textpage/add_comments.html'  
#     #success_url = reverse_lazy('textpage:textpage')
def addCom(request, pk):
    if request.method == 'POST':
        print("ここは通っている1")
        tcomf = TcomForm(request.POST, request.FILES)
        print(pk)
        text = Texts.objects.get(text_id=pk)
        tcomf = Tcom(text_id = text, user_id = request.user, date = timezone.now(),comments = tcomf.data.get("comments"))
        print(tcomf)
        tcomf.save()
<<<<<<< HEAD
        return render(self.request, 'textpage/textpage.html')

    def get_initial(self):
        print("ここは通っている2")
        #tcomf = TcomForm(self.request.POST, self.request.FILES)
        initial = super().get_initial()
        initial["text_id"] = self.kwargs['pk']
        initial["user_id"] = self.request.user
        return initial

        


=======
        tcom_list = Tcom.objects.order_by('date').reverse().all()
        return render(request, 'textpage/textpage.html', {
            'texts': text,
            'tcom_list':tcom_list,
            })

    form = TcomForm()
    return render(request, 'textpage/add_comments.html', {
        "form":form
    })

    # def get_initial(self):
    #     print("ここは通っている2")
    #     print("================",self.kwargs['pk'])
    #     #tcomf = TcomForm(self.request.POST, self.request.FILES)
    #     initial = super().get_initial()
    #     initial["text_id"] = self.kwargs['pk']
    #     initial["user_id"] = self.request.user
    #     return initial
>>>>>>> 57587317609de64135fc6a05e95b5e5a4180ee25
    

    # def get_success_url(self, **kwargs):
    #     return reverse_lazy('textpage:textpage', kwargs={'pk':self.kwargs['pk']})







  



        



      













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
