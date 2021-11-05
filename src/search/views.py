from django.shortcuts import render
from django.http import HttpResponse
from users.models import Classes, Texts
from django.db.models import Q, Avg


def index(request):
    q_class = request.POST.get('q_class')
    classes = Classes.objects.all()
    if q_class:
        queries = q_class.split()
        for query in queries:
            classes.append = classes.filter(
                Q(title__icontains=query)|
                Q(teacher__icontains=query)|
                Q(contents__icontains=query)
                ).distinct()
    else:
        classes = classes.order_by()
    return render(request, "search/index.html", {
        'classes':classes,
    })