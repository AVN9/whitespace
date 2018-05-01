# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
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
    paginator = Paginator(article_list, 5)
    
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

# for printing a single article using its id
def article_page(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'blog/blog_article.html', {'article' : article})