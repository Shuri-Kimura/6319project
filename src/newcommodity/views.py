from django.shortcuts import render
from users.models import Texts
from django.contrib import messages
from django.views import generic


def index(request):
  content = {
  'message': 'こんにちは！Djangoテンプレート！'
  }
  return render(request, 'newcommodity/newcommodity.html', content)

#from django.http import HttpResponse
class NewcommodityView(generic.CreateView):
    template_name = 'newcommodity/newcommodity.html'
    model= Texts
    fields='__all__'

    
    success_url = "http://127.0.0.1:8000/mypage/"  # 成功時にリダイレクトするURL
    def form_valid(self, form):
        ''' バリデーションを通った時 '''
        messages.success(self.request, "保存しました")
        return super().form_valid(form)

    def form_invalid(self, form):
        ''' バリデーションに失敗した時 '''
        messages.warning(self.request, "保存できませんでした")
        return super().form_invalid(form)
    #def get_queryset(self):
      # return Texts.objects.filter(text_id__gte=2)
       #less than equal(great)


#def index(request):
    #return HttpResponse("Hello, world. 6319project.newcommodity")
