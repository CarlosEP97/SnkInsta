"""Posts models."""

# Django
from django.db import models
from django.contrib.auth.models import User
# from snkinsta.users.models import Profile


class Post(models.Model):
    """Post model."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)


    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')
    likes = models.ManyToManyField(User,related_name='post_likes',blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return title and username."""
        return f'{self.title} by @{self.user.username}'