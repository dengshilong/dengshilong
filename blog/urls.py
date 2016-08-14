from django.conf.urls import url
from django.contrib.sitemaps.views import sitemap
from . import views, api
from .views import PostDetail, PostList, SitemapList, CategoryList, TagList, ArchiveList, PageDetail
from .feeds import LatestEntriesFeed
from .sitemaps import BlogSitemap
from django.views.generic import TemplateView

sitemaps = {
    'static': BlogSitemap,
}
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
    url(r'^api/blog/posts/list/?$', api.PostListAPI.as_view(), name='blog_post_api_list'),
    url(r'^api/blog/posts/(?P<pk>\d+)/?$', api.PostAPI.as_view(), name='blog_post_api'),
    url(r'^api/blog/category/(?P<category>\w+)/?$', api.CategoryAPI.as_view(), name='blog_category_api_list'),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),

]
