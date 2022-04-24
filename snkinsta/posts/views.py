
"""Posts views."""
# Django
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required # The login_required decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from django.http import HttpResponse
#model

from .models import Post

#Forms

from .forms import PostForm

# Utilities
from datetime import datetime



# @login_required # podemos acceder al feed si tenemos un sesion activa
# def list_posts(request):
#     """List existing posts."""
#     posts = Post.objects.all().order_by('-created')
#
#     return render(request, 'posts/feed.html', {'posts': posts})

class PostsFeedView(LoginRequiredMixin, ListView):
    """Return all published posts."""

    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 6
    context_object_name = 'posts'



@login_required
def create_post(request):
    """""create new post view"""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # post = form.save(commit=False)
            # post.user = request.user
            # post.profile = request.user.profile
            # post.save()
            return redirect('posts:feed')

    else:
        form = PostForm()

    return render(request,'posts/new.html',{'form':form, 'user': request.user, 'profile': request.user.profile})
