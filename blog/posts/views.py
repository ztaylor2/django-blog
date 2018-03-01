"""Views for posts app."""
from django.views.generic import TemplateView, CreateView, UpdateView
from posts.models import Post
from django.urls import reverse_lazy


class CreateView(CreateView):
    """Create view."""

    template_name = 'posts/create.html'
    model = Post
    fields = ['title', 'body']
    success_url = reverse_lazy('home')


class UpdateView(UpdateView):
    """Update a blogpost."""

    template_name = 'posts/edit.html'
    model = Post
    fields = ['title', 'body']
    success_url = reverse_lazy('home')


class DetailView(TemplateView):
    """Detail view."""

    template_name = 'posts/detail.html'
