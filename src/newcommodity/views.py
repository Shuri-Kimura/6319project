from django.shortcuts import render
from users.models import Texts
from django.contrib import messages
from django.views import generic
from .forms import TextForm


#～～～～～～～～～～～～～～～～～
# 新規登録フォームHTMLへ返す
def showCreateTextForm(request):
    #フォームを変数にセット
    form = TextForm()
 
    context = {
      'message': 'こんにちは！Djangoテンプレート！',
      'textForm':form,
    }
 
    #detail.htmlへデータを渡す
    return render(request, 'newcommodity/newcommodity.html',context)



#～～～～～～～～～～～～～～～～～

# フォームから受取ったデータをDBに登録する
def addText(request):
    #リクエストがPOSTの場合
    if request.method == 'POST':
        #リクエストをもとにフォームをインスタンス化
        textForm = TextForm(request.POST)
        if textForm.is_valid():
            textForm.save()
 
    #user.htmlへデータを渡す
    return render(request, 'mypage/mypage.html')

"""
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
"""