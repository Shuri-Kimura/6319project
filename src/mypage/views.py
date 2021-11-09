from django.http import HttpResponse,HttpResponseRedirect
from django.views import generic
from django.shortcuts import render
from users.models import Users
from django.utils import timezone

def mypage(request):
    return render(request, 'mypage/mypages.html')
class IndexView(generic.ListView):
    template_name = 'mypage/index.html'
    context_object_name = 'users_list'

    def get_queryset(self):
        return Users.objects.filter(user_id__isnull = False)

class MypageView(generic.DetailView):
    model = Users
    template_name = 'mypage/mypage.html'

def edit(request):
    return render(request,'mypage/edit.html')
