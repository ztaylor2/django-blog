"""URLS for admin login."""
from django.conf.urls import url
from posts.views import CreateView, DetailView

urlpatterns = [
    url(r'^create/$',
        CreateView.as_view(),
        name='create'),
    url(r'^detail/$',
        DetailView.as_view(),
        name='detail'),
]
