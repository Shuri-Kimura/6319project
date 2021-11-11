from django.shortcuts import render
from django.http import HttpResponse
from users.models import Classes, Texts, Cevals
from django.db.models import Q, Avg


def index(request):
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
    else:
        classes = Classes.objects.all().annotate(Avg('cevals__rikai')).annotate(Avg('cevals__raku'))
        texts = {}
    return render(request, "search/index.html", {
        'classes':classes,
        'texts':texts,
    })