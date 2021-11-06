from django.shortcuts import render
from django.http import HttpResponse
from users.models import Classes, Texts
from django.db.models import Q


def index(request):
    q_class = request.POST.get('q_class')
    q_text = request.POST.get('q_text')
    print(q_class)
    print(q_text)
    if q_class:
        classes = Classes.objects.all()
        queries = q_class.split()
        for query in queries: #今はキーワードで絞りまくってる。
            classes = classes.filter(
                Q(title__icontains=query)|
                Q(teacher__icontains=query)|
                Q(contents__icontains=query)
                ).distinct()
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
        classes = Classes.objects.all()
        classes = classes.order_by()
    return render(request, "search/index.html", {
        'classes':classes,
        'texts':texts,
    })