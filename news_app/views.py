from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator


def index(request):

    query = ''
    if request.GET.get('query'):
        query = request.GET.get('query')

    rows = News.objects.all().filter(title__contains=query).order_by("-created_at")
    paginator = Paginator(rows, 5)
    
    page_number = 1
    
    if request.GET.get('page'):
        page_number = int(request.GET.get('page'))

    next_page = page_number + 1 if (page_number + 1) <= len(paginator.page_range) else page_number
    previous_page = page_number - 1 if (page_number - 1) != 0 else page_number

    top_views = News.objects.all().order_by("-counter")[:5]
    new_news = News.objects.all().order_by("-created_at")[:4]
    # отправьте на страницу и разместите

    context = {
        'rows': paginator.page(page_number),
        'pages': paginator.page_range,
        'top_views':top_views,
        'new_news': new_news,
        "next_page": next_page,
        "previous_page" : previous_page
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

    comments = Comments.objects.filter(newsObject__id=id)

    context = {
        "row":row,
        "images":images,
        'rows':rows,
        'comments':comments
    }
    return render(request, "single.html", context)


def about(request):
    rows = Gallery.objects.all()
    context = {
        "rows":rows
    }
    return render(request, "about.html", context)



def paginationTest(request):
    rows = ['Бактияр', "Алинур", "Элянора", "Назик"]
    p = Paginator(rows, 3)
    # Paginator() принимает два аргумента, строки для пагинации и сколько в одной странце будет строк
    # функция page() возвращает страницу
    # page_range() возвращает нумерацию страниц

    page_number = 1

    if request.GET.get('page'):
        page_number = int(request.GET.get('page'))

    context = {
        "rows": p.page(page_number),
        "pages": p.page_range
    }
    return render(request, "PaginationTest.html", context)


def search(request):
    query = request.GET.get('query')
    rows = News.objects.filter(title__contains=query)
    context = {
        "rows": rows
    }
    return render(request, "search.html", context)

def like(request):
    id = request.GET.get('id')
    row = News.objects.get(id=id)
    row.like_count += 1
    row.save()
    return index(request)

def comments(request, id):
    name = request.POST.get('name')
    text = request.POST.get('text')
    row = News.objects.get(id=id)
    Comments.objects.create(newsObject=row, name=name, text=text)
    return single(request, id)
