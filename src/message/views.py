from django.shortcuts import render
from django.views import generic
from django.shortcuts import render, redirect
from users.models import Users, Messages, Uevals
from django.utils import timezone
from django.urls import reverse, reverse_lazy
from .forms import UevalFrom
# Create your views here.


class MessageList(generic.DetailView):
    model = Users
    template_name = 'message/message.html'

    def get_context_data(self, **kwargs):
        context = super(MessageList, self).get_context_data(**kwargs)
        context.update({
            'messages_list': Messages.objects.filter(ToUser=self.request.user.user_id),
        })
        return context


class MessageDetail(generic.DetailView):
    model = Messages
    template_name = 'message/detail.html'


def UserEvaluate(request, pk, to_pk):
    ToUser = Users.objects.get(user_id=to_pk)
    message = Messages.objects.get(message_id=pk)
    message = Messages(
        message_id=message.message_id,
        title=message.title,
        messages=message.messages,
        FromUser=message.FromUser,
        ToUser=message.ToUser,
        Eval_flag=1,
        date=message.date
    )
    message.save()
    if request.method == 'POST':
        Eval = UevalFrom(request.POST, request.FILES)
        Eval = Uevals(user_id=ToUser, eval=Eval.data.get('eval'))
        Eval.save()
        return redirect('message:detail', pk)
    form = UevalFrom()
    return render(request, 'message/UserEvaluate.html', {
        'form': form,
    })
