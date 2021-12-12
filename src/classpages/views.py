from django.db import models
from django.db.models import fields
from django.utils import timezone
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .forms import CcomForm,CevalForm,CreateForm
from users.models import Classes,Users,Cevals,Ccom
from django.urls import reverse

def index(request):
    return render(request, 'users/index.html')

#class IndexView(generic.ListView):
    template_name = 'classpages/index.html'
    context_object_name = 'classes_list'

    def get_queryset(self):
        return Classes.objects.filter(class_id__isnull = False)

class Classpage(generic.DetailView,generic.edit.ModelFormMixin):
    model = Classes
    template_name = 'classpages/class.html'
    form = CevalForm()
    fields = ()
    def get_context_data(self, **kwargs):
        context = super(Classpage, self).get_context_data(**kwargs)
        context.update({
            'avg': Cevals.objects.values('class_id').annotate(avg_rikai=models.Avg('rikai'),avg_raku=models.Avg('raku')),
            'ccom_list': Ccom.objects.order_by('date').reverse().all()[:5],
        })
        return context
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            eform = CevalForm(request.POST, request.FILES)
            cl = Classes.objects.get(class_id=self.kwargs['pk'])
            print(cl.class_id)
            eform = Cevals(class_id = cl, user_id = request.user, rikai = eform.data.get("rikai"), raku = eform.data.get("raku"))
            eform.save()
            return HttpResponseRedirect(reverse('classpages:class', args=(cl.class_id,)))
        form = CevalForm(**self.get_form_kwargs())
        return render(request, 'classpages:class', {
            "form":form
        })

    #def get_cfavo():
        #cfavo_list = Cevals.objects.filter(class_id__exact = Classes.objects.class_id)

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

def createclass(request):
    template_name = 'classpages/create.html'
    ctx = {}
    if request.method == 'GET':
        form = CreateForm()
        return render(request, template_name, {
            "form":form
        })
    if request.method == 'POST':
        create_form = CreateForm(request.POST)
        if create_form.is_valid():
            create_form.save()
            return HttpResponseRedirect(reverse('search:index'))
        else:
            ctx['form'] = create_form
            return render(request, template_name, ctx)
        