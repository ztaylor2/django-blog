"""Views for posts app."""
from django.views.generic import TemplateView


class CreateView(TemplateView):
    """Create view."""

    template_name = 'posts/create.html'


class DetailView(TemplateView):
    """Detail view."""

    template_name = 'posts/detail.html'
