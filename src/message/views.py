from django.shortcuts import render
from django.views import generic
from django.shortcuts import render
from users.models import Users, Messages
from django.utils import timezone
from django.urls import reverse, reverse_lazy
# Create your views here.


class MessageList(generic.DetailView):
    model = Users
    template_name = 'message/message.html'

    def get_context_data(self, **kwargs):
        context = super(MessageList, self).get_context_data(**kwargs)
        context.update({
            'messages_list': Messages.objects.filter(user_id=self.request.user.user_id),
        })
        return context


class MessageDetail(generic.DetailView):
    model = Messages
    template_name = 'message/detail.html'
