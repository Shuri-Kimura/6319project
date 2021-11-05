from django.shortcuts import render
from django.http import HttpResponse
from users.models import *

def like(request):
    return render(request, 'like/like.html')

def likely(request):
    return render(request, 'like/likely.html')

