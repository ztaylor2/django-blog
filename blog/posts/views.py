"""Views for posts app."""
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from posts.models import Post
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class CreateView(LoginRequiredMixin, CreateView):
    """Create view."""

    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    template_name = 'posts/create.html'
    model = Post
    fields = ['title', 'body']
    success_url = reverse_lazy('home')


class UpdateView(LoginRequiredMixin, UpdateView):
    """Update a blogpost."""

    login_url = '/login/'
    redirect_field_name = 'redirect_to'

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


class PostDelete(DeleteView):
    """The Delete View."""

    model = Post
    success_url = reverse_lazy('home')
