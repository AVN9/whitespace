# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Article, User

# Create your views here.
def index(request):
    return render(request, 'blog/blog_home.html', {})

# for printing articles
def articles(request):
    article_list = Article.objects.all()
    # listing only 10 articles per page
    paginator = Paginator(article_list, 10)
    
    page_req = request.GET.get('page')
    try:
        articles = paginator.page(page_req)
    except PageNotAnInteger:
        # if page is not an integer deliver first page
        articles = paginator.page(1)
    except EmptyPage:
        # in case out of pages, deliver last page
        articles = paginator.page(paginator.num_pages)
    return render(request, 'blog/blog_all_articles.html', {'articles' : articles})