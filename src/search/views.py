from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from users.models import Classes, Texts, Cevals, Tfavos
from django.db.models import Q, Avg


def index(request):
    if request.user.is_anonymous:#loginしていない場合勝手にloginページ
        return redirect('users:index')
    q_class = request.POST.get('q_class')
    q_text = request.POST.get('q_text')
    if q_class:
        classes_ = Classes.objects.all()
        queries = q_class.split()
        for query in queries: #今はキーワードで絞りまくってる。
            classes_ = classes_.filter(
                Q(title__icontains=query)|
                Q(teacher__icontains=query)|
                Q(contents__icontains=query)
                ).distinct()
        texts = {}
        classes = classes_.annotate(Avg('cevals__rikai')).annotate(Avg('cevals__raku'))
        #print(classes[0].cevals__raku__avg)
        liked_list = []
    elif q_text:
        texts = Texts.objects.all()
        queries = q_text.split()
        #queryからid所得そのidでfillter
        for query in queries:
            texts = texts.filter(
                Q(title__icontains=query)|
                Q(info__icontains=query)
                ).distinct()
        classes = {}
        liked_list = []
        for text in texts:
            liked = text.tfavos_set.filter(user_id=request.user)
            if liked.exists():
                liked_list.append(text.text_id)
        print(liked_list)
    else:
        classes = Classes.objects.all().annotate(Avg('cevals__rikai')).annotate(Avg('cevals__raku'))
        texts = {}
        liked_list = []
    return render(request, "search/index.html", {
        'classes':classes,
        'texts':texts,
        'liked_list': liked_list,
    })

def TlikeView(request):
    if request.method =="POST":
        #print(print(request.is_ajax()))
        text = get_object_or_404(Texts, pk=request.POST.get('text_id'))
        user = request.user
        liked = False
        #print(text)
        tfavos = Tfavos.objects.filter(text_id=text, user_id=user)
        if tfavos.exists():
            tfavos.delete()
        else:
            tfavos.create(text_id=text, user_id=user)
            liked = True
    
        context={
            'text_id': text.text_id,
            'liked': liked,
            'count': text.tfavos_set.count(),
        }

    if request.is_ajax():
        return JsonResponse(context)