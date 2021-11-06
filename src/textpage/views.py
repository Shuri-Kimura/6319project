from django.shortcuts import render
from django.http import HttpResponse
from users.models import Classes, Texts
from django.db.models import Q, Avg


def index(request):
    text ={
     'explain' : '二枚目を見てください'
    }
    q_class = request.POST.get('q_class')
    classes = Classes.objects.all()
    if q_class:
        queries = q_class.split()
        for query in queries:
            classes.append = classes.filter(
                Q(title__icontains=query)|
                Q(teacher__icontains=query)|
                Q(contents__icontains=query)
                ).distinct()
    else:
        classes = classes.order_by()
    return render(request, "index.html",{
        'classes':classes,
        'explain' : '二枚目を見てください',
    })

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
