"""Platzigram middleware catalog."""
# Middleware is a framework of hooks into Django’s request/response processing. It’s a light, low-level “plugin” system for globally altering Django’s input or output.
# Django
from django.shortcuts import redirect
from django.urls import reverse


class ProfileCompletionMiddleware:
    """Profile completion middleware.

    Ensure every user that is interacting with the platform
    have their profile picture and biography.
    """

    def __init__(self, get_response):
        #da acceso a la view antes de que el request lo haga, y nos puede ayudar a hacer checks en la data
        # o en el request antes y despues de que llegue a la view
        """Middleware initialization."""
        self.get_response = get_response

    def __call__(self, request):
        """Code to be executed for each request before the view is called."""
        if not request.user.is_anonymous:
            # request.user y request.user.profile sirve para traer los one to one fields
            # (de user traemos profile y de profile traemos user eso es un modelos one to one)
            # y tambien para traer el usuario que en ese momento este logueado y el perfil de esee usuario
            if not request.user.is_staff:
                profile = request.user.profile
                if not profile.picture or not profile.biography:
                    if request.path not in [reverse('users:update_profile'), reverse('users:logout')]:
                        return redirect('users:update_profile')

        response = self.get_response(request)
        return response