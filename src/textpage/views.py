from typing import TextIO
from django.db.models.query import QuerySet
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.db import models
from django.http import HttpResponse, HttpResponseRedirect, request
from django.urls.base import reverse_lazy
from django.views.generic.list import ListView
from django.views import generic
from django.db.models import Q
from django.shortcuts import render
from users.models import Target, Users
from .forms import MessageForm, TcomForm
from users.models import Tfavos, Cfavos, Classes, Texts, Tcom, Messages


class TextpageView(generic.DetailView):
    template_name = 'textpage/textpage.html'

    model = Texts

    def get_context_data(self, **kwargs):
        context = super(TextpageView, self).get_context_data(**kwargs)
        context.update({
            'tcom_list': Tcom.objects.order_by('date').reverse().all(),

        })
        return context


def TransActionList(request, pk):
    return render(request, 'textpage/TransActionList.html', {
        'target_list': Target.objects.filter(text_id=Texts.objects.get(text_id=pk)),
        'text': Texts.objects.get(user_id=request.user.user_id)
    })


def TransAction(request, text_pk, user_pk):
    text = Texts.objects.get(text_id=text_pk)
    if request.method == 'POST':
        messageF = MessageForm(request.POST, request.FILES)
        ToUser = Users.objects.get(user_id=user_pk)
        messageF = Messages(title=text.title, messages=request.user.username + "から教材の出品を受け取りましたよ",
                            user_id=ToUser, date=timezone.now())
        print(messageF)
        messageF.save()
        tcom_list = Tcom.objects.order_by('date').reverse().all()
        return render(request, 'textpage/textpage.html', {
            'texts': text,
            'tcom_list': tcom_list,
        })

    form = MessageForm()
    return render(request, 'textpage/TransAction.html', {
        'form': form,
        'text': text
    })
# class AddCom(generic.CreateView):
#     fields = '__all__'
#     model = Tcom
#     template_name = 'textpage/add_comments.html'
#     #success_url = reverse_lazy('textpage:textpage')

# 教材に対する新しいコメントの追加
# やっている事1
# 新しいコメントの追加
# やっている事2
# Targetテーブルに新しいToUserを追加
# ただし、既に同じToUserが存在すれば、追加は省く


def addCom(request, pk):
    if request.method == 'POST':
        print("ここは通っている1")
        tcomf = TcomForm(request.POST, request.FILES)
        print(pk)
        TF = True
        text = Texts.objects.get(text_id=pk)
        tcomf = Tcom(text_id=text, user_id=request.user,
                     date=timezone.now(), comments=tcomf.data.get("comments"))
        # tarにTargetテーブルのToUserがrequest.userに対応するものだけを抽出
        tar = Target.objects.filter(ToUser=request.user)
        for inner in tar:
            if inner.ToUser == request.user:
                TF = False
        if text.user_id != request.user and TF:
            target = Target(ToUser=request.user, text_id=text)
            # ここでtargetを追加
            target.save()
        print(tcomf)
        # ここでtcomfを追加
        tcomf.save()
        tcom_list = Tcom.objects.order_by('date').reverse().all()
        return render(request, 'textpage/textpage.html', {
            'texts': text,
            'tcom_list': tcom_list,
        })

    form = TcomForm()
    return render(request, 'textpage/add_comments.html', {
        "form": form
    })

    # def get_initial(self):
    #     print("ここは通っている2")
    #     print("================",self.kwargs['pk'])
    #     #tcomf = TcomForm(self.request.POST, self.request.FILES)
    #     initial = super().get_initial()
    #     initial["text_id"] = self.kwargs['pk']
    #     initial["user_id"] = self.request.user
    #     return initial

    # def get_success_url(self, **kwargs):
    #     return reverse_lazy('textpage:textpage', kwargs={'pk':self.kwargs['pk']})


# def index(request):
 # content = {
  # 'message': 'こんにちは！Djangoテンプレート！'
  # }
  # return render(request, 'index.html', content)


#from django.http import HttpResponse
#from django.views.generic import TemplateView


# class IndexView(TemplateView):
    #template_name = "index.html"


# def index(request):

    # return HttpResponse("Hello, world. 6319project.textpage")
# Create your views here.
