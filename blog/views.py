# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, User

# Create your views here.
def index(request):
    return render(request, 'blog/blog_home.html', {})

# for printing articles
def articles(request):
    article_obj = Article.objects.all()[:10]
    return render(request, 'blog/blog_all_articles.html', { 'articles' : article_obj})