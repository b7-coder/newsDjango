from django.shortcuts import render
from .models import *

def index(request):
    rows = News.objects.all()
    # извлечь все
    # select * from News;

    top_views = News.objects.all().order_by("-counter")[:5]
    # пять отсортированных строк по убыванию
    # my_list = [0,0,0,0,0,0,0]
    # my_list[0]
    # my_list[0:5]
    # my_list[0:5:2]

    context = {
        'rows':rows,
        'top_views':top_views
    }
    return render(request, 'index.html', context)

def single(request, id):
    row = News.objects.get(id = id) 
    # извлечение строки по id
    # аналог select * from News where id = id limit 1;

    images = NewsImages.objects.filter(newsObject__id=id)
    
    rows = NewsDetails.objects.filter(newsObject__id=id)

    row.counter = row.counter + 1
    row.save()

    context = {
        "row":row,
        "images":images,
        'rows':rows
    }
    return render(request, "single.html", context)


def about(request):
    rows = Gallery.objects.all()
    context = {
        "rows":rows
    }
    return render(request, "about.html", context)
