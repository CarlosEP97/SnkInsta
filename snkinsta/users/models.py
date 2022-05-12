from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    """Profile model.

    Proxy model that extends the base data with other
    information.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE) # this relation allows to user acces to the profile
    # and make uses of followers field

    website = models.URLField(max_length=200, blank=True)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    picture = models.ImageField(
        upload_to='users/pictures',
        blank=True,
        null=True
    )
    followers = models.ManyToManyField(User,related_name='following',blank=True)
    # a user profile  can acces to his followers and a user can acces to following user
    # user -> profile -> can see followers and add followers for each userProfile
    # user -> folling _> can see followings

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return username."""
        return self.user.username
