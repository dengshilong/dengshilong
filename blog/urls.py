from django.conf.urls import url
from django.contrib.sitemaps.views import sitemap
from . import views
from .feeds import LatestEntriesFeed
from .sitemaps import BlogSitemap
sitemaps = {
    'static': BlogSitemap,
}
urlpatterns = [
    url(r'^$', views.index, name='blog.index'),
    url(r'^sitemap/$', views.sitemap_view, name='blog.sitemap_view'),
    url(r'^(\d+)/(\d+)/(\d+)/(.+)/$', views.post, name="blog.post"),
    url(r'^(\d+)/(\d+)/$', views.archive, name="blog.archive"),
    url(r'category/(.+)/$', views.category, name="blog.category"),
    url(r'tag/(.+)/$', views.tag, name="blog.tag"),
    url(r'^feed/$', LatestEntriesFeed()),
    url(r'(.+)/$', views.page, name="blog.page"),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap')
]
