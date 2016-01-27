from django.conf.urls import url
from . import views
from .feeds import LatestEntriesFeed
urlpatterns = [
    url(r'^$', views.index, name='blog.index'),
    url(r'^(\d+)/(\d+)/(\d+)/(.+)/$', views.post, name="blog.post"),
    url(r'^(\d+)/(\d+)/$', views.archive, name="blog.archive"),
    url(r'category/(.+)/$', views.category, name="blog.category"),
    url(r'tag/(.+)/$', views.tag, name="blog.tag"),
    url(r'^feed/$', LatestEntriesFeed()),
    url(r'(.+)/$', views.page, name="blog.page"),
]
