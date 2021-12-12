from django.db import models
from django.db.models import fields
from django.utils import timezone
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .forms import CcomForm
from users.models import Classes,Users,Cevals,Ccom
from django.urls import reverse

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
            'ccom_list': Ccom.objects.order_by('date').reverse().all(),
        })
        return context
    #def get_cfavo():
        cfavo_list = Cevals.objects.filter(class_id__exact = Classes.objects.class_id)

def addccom(request, pk):
    if request.method == 'POST':
        print("ここは通っている1")
        ccomf = CcomForm(request.POST, request.FILES)
        print(pk)
        cl = Classes.objects.get(class_id=pk)
        ccomf = Ccom(class_id = cl, user_id = request.user, date = timezone.now(),comments = ccomf.data.get("comments"))
        print(ccomf)
        ccomf.save()
        ccom_list = Ccom.objects.order_by('date').reverse().all()
        return HttpResponseRedirect(reverse('classpages:class', args=(cl.class_id,)))
        #return render(request, 'classpages/class.html', {
            #'texts': cl,
            #'ccom_list':ccom_list,
            #})

    form = CcomForm()
    return render(request, 'classpages/add_comments.html', {
        "form":form
    })

        