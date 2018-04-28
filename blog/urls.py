from django.conf.urls import url
from . import views
app_name = "blog"

urlpatterns = [
    url(r'^$', views.index, name="blog_index"),
    url(r'^articles/', views.articles, name="all_articles"),    
]