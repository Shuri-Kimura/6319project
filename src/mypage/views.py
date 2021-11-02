from django.http import HttpResponse,HttpResponseRedirect
from django.views import generic
from django.shortcuts import render

def mypage(request):
    return render(request, 'mypage/mypage.html')

def edit(request):
    return render(request,'mypage/edit.html')