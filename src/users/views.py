#from django.http import HttpResponse
from django.shortcuts import render


#def index(request):
 #   return HttpResponse("Hello, world. 6319project.mypage")

def index(request):
    return render(request, 'users/index.html')