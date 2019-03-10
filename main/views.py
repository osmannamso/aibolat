from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .models import Author, New, Category


def author_news(request, id):
    news = New.objects.filter(author_id=id).values()
    return JsonResponse({'news': list(news)})


def category_news(request, id):
    news = New.objects.filter(categories__id=id).values()
    return JsonResponse({'news': list(news)})


def authors(request):
    authors = Author.objects.all().values()
    return JsonResponse({'authors': list(authors)})


def new(request, id):
    new = New.objects.filter(pk=id).values()
    return JsonResponse({'new': list(new)})


def search_new(request, name):
    news = New.objects.filter(title__icontains=name).values()
    return JsonResponse({'news': list(news)})


def category_daughter_news(request, id):
    cats = list()
    category = Category.objects.get(pk=id)
    categoreis = Category.objects.filter(parent=category)
    cats.append(category.id)
    for q in categoreis:
        cats.append(q.id)

    news = New.objects.filter(categories__id__in=cats).values()

    return JsonResponse({'news': list(news)})


def add_new(request, title, context, author, categories):
    cats = []
    q = ''
    for c in categories:
        if c == ',':
            cats.append(int(q))
        else:
            q += c
    auth = Author.objects.get(pk=author)
    new = New(title=title, context=context, author=auth)
    new.save()
    lala = Category.objects.filter(id__in=cats)
    for c in lala:
        new.categories.add(c)
    new.save()

    naix = New.objects.filter(pk=new.id).values()

    return JsonResponse({'new': list(naix)})


def add_category(request, name, id):
    parent = id
    if parent != 'None':
        parent = int(parent)
        par = Category.objects.get(pk=parent)
        cat = Category(name=name, parent=par)
    else:
        cat = Category(name=name, parent=None)
    cat.save()

    cats = Category.objects.filter(pk=cat.id).values()

    return JsonResponse({'category': list(cats)})


def add_author(request, name, avatar):
    author = Author(name=name, avatar=avatar)
    author.save()

    authors = Author.objects.filter(pk=author.id).values()

    return JsonResponse({'author': list(authors)})
