from django.conf.urls import url
from . import views


urlpatterns = [
        url(r"^$", views.index, name='index'),
        url(r"^about/$", views.about, name='about'),
        url(r'^blog/$', views.blogs, name='blogs'),
        url(r"^blog/(?P<post_name>[\w\-]+)$", views.post, name='post'),
        url(r"tag/(?P<tag_name>[\w\-]+)$", views.tag, name='tag'),
]
