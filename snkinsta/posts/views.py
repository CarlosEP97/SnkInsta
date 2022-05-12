
"""Posts views."""
# Django
from django.urls import reverse_lazy,reverse
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required # The login_required decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,DetailView,CreateView

from django.http import HttpResponse
#model

from .models import Post
from django.contrib.auth.models import User


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
    # listview can get url parameters but not as slug or pk
    #output multiple objects
    # can be paginate
    template_name = 'posts/feed.html'
    model = Post # listView pone en el template toda la informacion del modelo con un queryset.all()
    ordering = ('-created',)
    paginate_by = 20
    context_object_name = 'posts'

class PostDetailView(LoginRequiredMixin, DetailView):
    """Return post detail."""
    # detail view can get url parameter as url or slug if we want also can get url parameters too
    # present detail of a sigle model instance
    #intented to be used with one object only
    #this recive a PK
    # pk_url_kwarg = 'pk'
    # query_pk_and_slug = 'pk'
    template_name = 'posts/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'


@login_required
def likes(request,pk):
    post = get_object_or_404(Post, pk=pk)
    is_like = False
    for like in post.likes.all():
        if like == request.user:
            is_like = True
            break
    if not is_like:
        post.likes.add(request.user)
    if is_like:
        post.likes.remove(request.user)
    next = request.POST.get('next','/')
    return HttpResponseRedirect(next)



class CreatePostView(LoginRequiredMixin, CreateView):
    # display a form for creating an object

    """Create a new post."""

    template_name = 'posts/new.html' # take a template
    form_class = PostForm # use a form
    success_url = reverse_lazy('posts:feed') # redirect to

    def get_context_data(self, **kwargs):
        """Add user and profile to context."""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user # user login in that time
        context['profile'] = self.request.user.profile # profile of user login in that time
        return context # contex to use in template


# @login_required
# def create_post(request):
#     """""create new post view"""
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             # post = form.save(commit=False)
#             # post.user = request.user
#             # post.profile = request.user.profile
#             # post.save()
#             return redirect('posts:feed')
#
#     else:
#         form = PostForm()
#
#     return render(request,'posts/new.html',{'form':form, 'user': request.user, 'profile': request.user.profile })
