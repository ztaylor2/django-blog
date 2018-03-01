"""URLS for admin login."""
from django.conf.urls import url
from posts.views import CreateView, DetailView, UpdateView, PostDelete

urlpatterns = [
    url(r'^create/$',
        CreateView.as_view(),
        name='create'),
    url(r'^detail/(?P<pk>\d+)/$',
        DetailView.as_view(),
        name='detail'),
    url(r'^update/(?P<pk>\d+)/$',
        UpdateView.as_view(),
        name='update'),
    url(r'^delete/(?P<pk>\d+)/$',
        PostDelete.as_view(),
        name='delete'),
]
