from django.db import models
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from users.models import Classes,Users,Cevals

def index(request):
    return render(request, 'users/index.html')

#class IndexView(generic.ListView):
    template_name = 'classpages/index.html'
    context_object_name = 'classes_list'

    def get_queryset(self):
        return Classes.objects.filter(class_id__isnull = False)

class Classpage(generic.DetailView):
    model = Classes
    template_name = 'classpages/class.html'
    def get_context_data(self, **kwargs):
        context = super(Classpage, self).get_context_data(**kwargs)
        context.update({
            'avg': Cevals.objects.values('class_id').annotate(avg_rikai=models.Avg('rikai'),avg_raku=models.Avg('raku')),
        })
        return context
    #def get_cfavo():
    #    cfavo_list = Cevals.objects.filter(class_id__exact = Classes.objects.class_id)