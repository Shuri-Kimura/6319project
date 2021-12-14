from django.shortcuts import render
from users.models import Texts, Classes
from django.contrib import messages
from django.views import generic
from .forms import TextForm


#～～～～～～～～～～～～～～～～～
# 新規登録フォームHTMLへ返す
def showCreateTextForm(request):
    #フォームを変数にセット
    form = TextForm()
 
    classes = Classes.objects.values()
    num = range(1,Classes.objects.count() + 1)
    for class_, i in zip(classes, num):
        class_["num"] = i
   
    return render(request, 'newcommodity/newcommodity.html',{
        'classes':classes,
        'textForm':form,
    })



#～～～～～～～～～～～～～～～～～

# フォームから受取ったデータをDBに登録する
def addText(request):
    #リクエストがPOSTの場合
    if request.method == 'POST':
        #リクエストをもとにフォームをインスタンス化
        textForm = TextForm(request.POST, request.FILES)
        print(textForm.is_valid())
        print(request.FILES)
        print("カテゴリー", textForm.data.get("category"))
        Class = Classes.objects.get(class_id=textForm.data.get("class_id"))
        textForm = Texts(user_id=request.user, class_id=Class, title=textForm.data.get("title"), info=textForm.data.get("info"), category=textForm.data.get("category"), state=textForm.data.get("state"), sold_flag=False, days=textForm.data.get("days"), image1=request.FILES.get("image1"), image2=request.FILES.get("image2"), image3=request.FILES.get("image3"))
        textForm.save()
        #user.htmlへデータを渡す
    #return render(request, 'mypage/mypage.html')
    return render(request, 'newcommodity/complete.html')


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