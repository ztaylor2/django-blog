"""URLS for admin login."""
from django.conf.urls import url
from posts.views import CreateView, DetailView, UpdateView

urlpatterns = [
    url(r'^create/$',
        CreateView.as_view(),
        name='create'),
    url(r'^detail/$',
        DetailView.as_view(),
        name='detail'),
    url(r'^update/(?P<pk>\d+)/$',
        UpdateView.as_view(),
        name='update'),
]
