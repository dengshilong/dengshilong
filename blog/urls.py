from django.conf.urls import url, include
from django.contrib.sitemaps.views import sitemap
from rest_framework import routers

from . import views, api
from .views import PostDetail, PostList, SitemapList, CategoryList, TagList, ArchiveList, PageDetail
from .feeds import LatestEntriesFeed
from .sitemaps import BlogSitemap
from django.views.generic import TemplateView

sitemaps = {
    'static': BlogSitemap,
}
router = routers.DefaultRouter()
router.register(r'links', views.LinkViewSet, base_name='links')
router.register(r'posts', views.PostViewSet, base_name='posts')
router.register(r'categories', views.CategoryViewSet, base_name='categories')
router.register(r'tags', views.TagViewSet, base_name='tags')

urlpatterns = [
    url(r'^$', PostList.as_view(), name='blog.index'),
    url(r'^sitemap/$', SitemapList.as_view(), name='blog.sitemap_view'),
    url(r'^(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/(?P<slug>.+)/$', PostDetail.as_view(), name="blog.post"),
    url(r'^(?P<year>\d+)/(?P<month>\d+)/$', ArchiveList.as_view(), name="blog.archive"),
    url(r'^category/(?P<category>.+)/$', CategoryList.as_view(), name="blog.category"),
    url(r'^tag/(?P<tag>.+)/$', TagList.as_view(), name="blog.tag"),
    url(r'^feed/$', LatestEntriesFeed()),
    url(r'^(?P<slug>[-\w]+)/$', PageDetail.as_view(), name="blog.page"),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^api/', include(router.urls)),
    url(r'^api/months', views.MonthsAPI.as_view(), name='months'),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),

]
