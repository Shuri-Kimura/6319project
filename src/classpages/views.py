from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from classpages.models import Classes

#def index(request):
    #return render(request,'classpages/index.html')
    
class IndexView(generic.ListView):
    template_name = 'classpages/index.html'
    context_object_name = 'classes_list'

    def get_queryset(self):
        return Classes.objects.filter(class_id__isnull = False)

class Classpage(generic.DetailView):
    model = Classes
    template_name = 'classpages/class.html'