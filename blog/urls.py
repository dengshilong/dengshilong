from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='blog.index'),
    url(r'^(\d+)/(\d+)/(\d+)/(.+)/$', views.post, name="blog.post"),
]
