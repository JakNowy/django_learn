from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # Where to redirect after creating a post with a generic view
    def get_absolute_url(self):
        # reverse, not redirect, cause only the string URL required
        return reverse('post-detail', kwargs={'pk':self.pk})