"""Views for blog app."""
from django.views.generic import ListView
from posts.models import Post


class HomeView(ListView):
    """Home page view."""

    template_name = 'blog/home.html'
    model = Post
    queryset = Post.objects.order_by('publication_date').reverse()
    paginate_by = 10

    def get_context_data(self, **kwargs):
        """Get data from post model."""
        context = super().get_context_data(**kwargs)

        body_previews = []
        for post in context['object_list']:
            body_previews.append((post.title, ' '.join(post.body.split()[:100]) + '...', post.publication_date, post.pk))

        context['body_previews'] = body_previews
        return context
