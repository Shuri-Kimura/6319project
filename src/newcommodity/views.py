from django.shortcuts import render



def index(request):
  content = {
  'message': 'こんにちは！Djangoテンプレート！'
  }
  return render(request, 'newcommodity/newcommodity.html', content)

#from django.http import HttpResponse


#def index(request):
    #return HttpResponse("Hello, world. 6319project.newcommodity")
