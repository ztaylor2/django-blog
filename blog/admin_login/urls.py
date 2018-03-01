"""URLS for admin login."""
from django.conf.urls import url
from admin_login.views import AdminLogin

urlpatterns = [
    url(r'^$',
        AdminLogin.as_view(),
        name='admin_login'),
]
