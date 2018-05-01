from django.conf.urls import url
from . import views
app_name = "blog"

urlpatterns = [
    
    # home - /home
    url(r'^$', views.index, name="blog_index"),
    
    # articles listing - /articles
    url(r'^articles/', views.articles, name="all_articles"),

    # specific article - /articles/100
    url(r'^article/(?P<article_id>[0-9]+)$', views.article_page, name="article_page"),

]