"""Views for posts app."""
from django.views.generic import CreateView, UpdateView, DetailView
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


class DetailView(DetailView):
    """Detail view."""

    template_name = 'posts/detail.html'
    model = Post

    def get_context_data(self, **kwargs):
        """Get data for detail view."""
        context = super().get_context_data(**kwargs)
        return context
