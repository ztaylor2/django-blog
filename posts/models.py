"""Database models for posts."""
from django.db import models


class Post(models.Model):
    """The database model for a blog post."""

    title = models.CharField(max_length=50)
    body = models.TextField()
    publication_date = models.DateField(auto_now_add=True)
