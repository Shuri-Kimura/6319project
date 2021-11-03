from django.http import HttpResponse,HttpResponseRedirect
from django.views import generic
from django.shortcuts import render

#from ..users.models import Cfavos, Tfavos

def like(request):
    return render(request, 'like/like.html')

def likely(request):
    return render(request, 'like/likely.html')

