from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from users.models import Tfavos

#def like(request):
  #  return render(request, 'like/like.html')

#def likely(request):
 #   return render(request, 'like/likely.html')


class LikeListView(ListView):
    template_name = 'like.html'
    model = Tfavos
