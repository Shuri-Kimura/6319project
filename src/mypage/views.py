from django.http import HttpResponse, HttpResponseRedirect
from django.db import models
from django.views import generic
from django.shortcuts import render
from users.models import Uevals, Users, Texts
from django.utils import timezone
from django.urls import reverse, reverse_lazy


def mypage(request):
    return render(request, 'mypage/mypages.html')


class IndexView(generic.ListView):
    template_name = 'mypage/index.html'
    context_object_name = 'users_list'

    def get_queryset(self):
        return Users.objects.filter(user_id__isnull=False)


class MypageView(generic.DetailView):
    model = Users
    template_name = 'mypage/mypage.html'

    def get_context_data(self, **kwargs):
        context = super(MypageView, self).get_context_data(**kwargs)
        context.update({
            'texts_list': Texts.objects.filter(user_id=self.request.user),
            'ueval_avg': Uevals.objects.filter(user_id=self.request.user).aggregate(avg=models.Avg('eval')),
            'quantity': Texts.objects.filter(user_id=self.request.user).count(),
        })
        return context


class MypageView2(generic.ListView):
    template_name = 'mypage/mypage.html'
    model = Users

    def get_context_data(self, **kwargs):
        context = super(MypageView2, self).get_context_data(**kwargs)
        context.update({
            'object_list2': Texts.objects.all(),
        })
        return context

    def get_queryset(self):
        return Users.objects.all()


class CommentUpdate(generic.edit.UpdateView):
    model = Users
    fields = ['username', 'user_comment', 'email', 'image']
    template_name = 'mypage/edit.html'


class DeleteList(generic.ListView):
    template_name = 'mypage/delete_list.html'
    context_object_name = 'texts_list'

    def get_queryset(self):
        return Texts.objects.filter(user_id=self.request.user)


class DeleteText(generic.DeleteView):
    model = Texts
    #success_url = reverse_lazy('mypage:mypage')

    def get_success_url(self):
        return reverse('mypage:mypage', kwargs={'pk': self.request.user.user_id})
    template_name = 'mypage/delete.html'


def edit(request):
    return render(request, 'mypage/edit.html')
