from typing import TextIO
from django.db.models.query import QuerySet
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.db import models
from django.http import HttpResponse, HttpResponseRedirect, request
from django.urls.base import reverse_lazy, reverse
from django.views.generic.list import ListView
from django.views import generic
from django.db.models import Q
from django.shortcuts import render
from users.models import Target, Uevals, Users
from .forms import MessageForm, TcomForm, TcomForm2, TextForm, UevalFrom
from users.models import Tfavos, Cfavos, Classes, Texts, Tcom, Messages
from django.core.mail import send_mail, EmailMessage


# class TextpageView(generic.DetailView):
#     template_name = 'textpage/textpage.html'

#     model = Texts

#     def get_context_data(self, **kwargs):
#         context = super(TextpageView, self).get_context_data(**kwargs)
#         context.update({
#             'tcom_list': Tcom.objects.order_by('date').reverse().all(),

#         })
#         return context
def TextpageView(request, pk):
    text = Texts.objects.get(text_id=pk)
    if request.user == text.user_id:
        form = TcomForm2()
    else:
        form = TcomForm()
    if request.method == 'POST':
        tcomf = TcomForm(request.POST, request.FILES)
        e_or_a = True
        if tcomf.data.get("exhibitor_or_all") == None:
            e_or_a = False
        TF = True
        tcomf = Tcom(
            text_id=text,
            user_id=request.user,
            exhibitor_or_all=e_or_a,
            date=timezone.now(),
            comments=tcomf.data.get("comments")
        )
        MessageF = MessageForm()
        if request.user != text.user_id:
            MessageF = Messages(
                title=request.user.username + 'が' + text.title + 'に対してコメントしました',
                messages=request.user.username + ':' + tcomf.comments,
                FromUser=request.user,
                ToUser=text.user_id,
                date=tcomf.date
            )
            MessageF.save()
        # tarにTargetテーブルのToUserがrequest.userに対応するものだけを抽出
        tar = Target.objects.filter(ToUser=request.user)
        for inner in tar:
            if inner.ToUser == request.user:
                TF = False
        if text.user_id != request.user and TF:
            target = Target(
                ToUser=request.user,
                text_id=text
            )
            # ここでtargetを追加
            target.save()
        # ここでtcomfを追加
        tcomf.save()
        return redirect('textpage:textpage', text.text_id)
    else:
        return render(request, 'textpage/textpage.html', {
            'texts': text,
            'tcom_list': Tcom.objects.order_by('date').reverse().all(),
            'form': form
        })


def TextUpdate(request, pk):
    text = Texts.objects.get(text_id=pk)
    initial_data = {
        'info': text.info,
        'category': text.category,
        'state': text.state,
        'days': text.days
    }
    if request.method == 'POST':
        textf = TextForm(request.POST, request.FILES)
        text = Texts(
            text_id=text.text_id,
            user_id=text.user_id,
            class_id=text.class_id,
            title=text.title,
            info=textf.data.get('info'),
            sold_flag=text.sold_flag,
            category=textf.data.get('category'),
            state=textf.data.get('state'),
            date=text.date,
            days=textf.data.get('days'),
            image1=text.image1,
            image2=text.image2,
            image3=text.image3,
        )
        text.save()
        return redirect('textpage:textpage', text.text_id)
    else:
        form = TextForm(initial=initial_data)
        return render(request, 'textpage/update.html', {
            'form': form,
            'text': text
        })


def TransActionList(request, pk):
    return render(request, 'textpage/TransActionList.html', {
        'target_list': Target.objects.filter(text_id=Texts.objects.get(text_id=pk)),
        'text': Texts.objects.get(text_id=pk)
    })


def UserEvaluate(request, text_pk, user_pk):
    text = Texts.objects.get(text_id=text_pk)
    ToUser = Users.objects.get(user_id=user_pk)
    if request.method == 'POST':
        Eval = UevalFrom(request.POST, request.FILES)
        Eval = Uevals(user_id=ToUser, eval=Eval.data.get('eval'))
        Eval.save()
        return redirect('textpage:TransAction', text.text_id, ToUser.user_id)
    form = UevalFrom()
    return render(request, 'textpage/UserEvaluate.html', {
        'form': form,
        'text': text,
        'ToUser': ToUser
    })


def TransAction(request, text_pk, user_pk):
    text = Texts.objects.get(text_id=text_pk)
    if request.method == 'POST':
        ToUser = Users.objects.get(user_id=user_pk)
        messageF = Messages(
            title=text.title,
            messages=request.user.username + "から教材の出品を受け取りましたよ",
            FromUser=text.user_id,
            ToUser=ToUser,
            Eval_flag=-1,
            date=timezone.now()
        )
        print(messageF)
        messageF.save()
        # メール送信処理
        send_mail(
            subject='トピック作成: ',
            message='トピックが作成されました。',
            from_email='tusproject7@gmail.com',
            recipient_list=[
                '6319011@ed.tus.ac.jp',
            ]
        )
        text = Texts(
            text_id=text.text_id,
            user_id=text.user_id,
            class_id=text.class_id,
            title=text.title,
            info=text.info,
            sold_flag=True,
            category=text.category,
            state=text.state,
            date=text.date,
            days=text.days,
            image1=text.image1,
            image2=text.image2,
            image3=text.image3,
        )
        text.clean()
        text.save()
        tcom_list = Tcom.objects.order_by('date').reverse().all()
        return redirect('textpage:textpage', text.text_id)
        # return render(request, 'textpage/textpage.html', {
        #     'texts': text,
        #     'tcom_list': tcom_list,
        # })

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
