"""Views for blog app."""
from django.views.generic import ListView
from posts.models import Post


class HomeView(ListView):
    """Home page view."""

    template_name = 'blog/home.html'
    model = Post

    def get_context_data(self, **kwargs):
        """Get data from post model."""
        context = super().get_context_data(**kwargs)
        if context['object_list']:
            body_preview = ' '.join(context['object_list'][0].body.split()[:100]) + '...'
        context['body_preview'] = body_preview
        return context
