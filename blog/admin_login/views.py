"""Views for admin login app."""
from django.views.generic import TemplateView


class AdminLogin(TemplateView):
    """Admin Login view."""

    template_name = 'admin_login/admin_login.html'
