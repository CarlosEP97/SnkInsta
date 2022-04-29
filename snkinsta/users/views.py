 # Create your views here.

"""Users views."""

# Django
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse,reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required # The login_required decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView,FormView,UpdateView
from django.views import View

#Django Models
from django.contrib.auth.models import User #ModelUser
from posts.models import Post
from users.models import Profile

#Django exceptions
from django.db.utils import IntegrityError

# Forms
from .forms import SignupForm


class UserDetailView(LoginRequiredMixin,DetailView):
    # detail view can get url parameter as url or slug if we want also can get url parameters too
    # present detail of a sigle model instance
    #intented to be used with one object only
    ''''user detailview'''
    template_name = 'users/detail.html' # recibe el template
    slug_field = 'username' # the name of the field on the model that contains the slug. By default, slug_field is 'slug'.
    #slug execute the queryset for find a user with that username.
    slug_url_kwarg = 'username' # The name of the URLConf keyword argument that contains the slug. By default, slug_url_kwarg is 'slug'.
    queryset = User.objects.all() # ese query recibe el username que entra en el slug o el parametro por url
    # The model that this view will display data for. ia specifying queryset
    #A QuerySet that represents the objects. If provided, the value of queryset supersedes the value provided for model.
    context_object_name = 'user' # Designates the name of the variable to use in the context.,Model name in template

    def get_context_data(self, **kwargs):
        print(self.queryset)
        # Returns context data for displaying the object.
        #The base implementation of this method requires that the self.object attribute be set by the view
        #While this view is executing, self.object will contain the object that the view is operating upon
        #self.objects is the model or the queryset instance of the model
        """Add user's posts to context."""
        context = super().get_context_data(**kwargs) #llama al metodo antes de ser sobre escrito,
        user = self.get_object() # If queryset is provided, that queryset will be used as the source of objects
        #Otherwise get_queryset() will be used
        context['posts'] = Post.objects.filter(user=user).order_by('-created')  # context is just a dictionary
        # print(context)
        return context


    # def get_object(self, queryset=None): # obtiene un objeto si no hay queryset
    #     user = User.objects.get(username = self.kwargs.get('username'))
    #     return user
    #
    # def get_context_data(self, **kwargs):
    #
    #     """Add user's posts to context."""
    #     context = super().get_context_data(**kwargs)
    #     context['posts'] = Post.objects.filter(user=self.get_object()).order_by('-created')
    #     return context



    # model = User
    # template_name = 'users/detail.html'
    # slug_field = 'username'
    # slug_url_kwarg = 'username'
    # context_object_name = 'user'
    #
    # def get_queryset(self):
    #     user = User.objects.all()
    #     return user
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     user = self.get_object()
    #     context['posts'] = Post.objects.filter(user=user).order_by('-created')
    #     return context


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    # retrieve specific object/data
    #add/update data base

    """Update profile view."""

    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website', 'biography', 'phone_number', 'picture']

    def get_object(self, queryset=None):
        """Return user's profile."""
        return self.request.user.profile  #objeto que va a actualizar , este query trae el profile

    def get_success_url(self):
        """Return to user's profile."""
        username = self.object.user.username # y este trae el username , self.object hace referencia al Profile
        # que traemos con el get_object
        return reverse('users:detail', kwargs={'username': username})

# @login_required
# def update_profile(request):
#         """Update a user's profile view."""
#         profile = request.user.profile # sessionMiddleware nos da la propiedad de acceder al request.user
#
#
#         if request.method == 'POST':
#             form = ProfileForm(request.POST, request.FILES) # Mandar diccionario de POST al formulario , es una instancia y va a tomar los datos de nuestro request
#             #se inicializa y se llena con los datos del POST.request
#             if form.is_valid():
#                 data = form.cleaned_data
#                 print(form.cleaned_data)
#
#                 profile.website = data['website']
#                 profile.phone_number = data['phone_number']
#                 profile.biography = data['biography']
#                 profile.picture = data['picture']
#                 profile.save()
#
#                 # url = reverse('users:detail', kwargs ={'username': request.user.username})
#                 # return redirect(url) # redirect no puede construir la URl como reverse
#                 return HttpResponseRedirect(reverse('users:detail', kwargs ={'username': request.user.username}))
#         else:                                                       # args = (request.user.username,)
#             form = ProfileForm()
#
#         return render(
#             request=request,
#             template_name='users/update_profile.html',
#             context={
#                 'profile': profile,
#                 'user': request.user,
#                 'form': form
#             }
#         )


class LoginView(auth_views.LoginView):
    """Login view."""

    template_name = 'users/login.html'
    redirect_authenticated_user = True




# def login_view(request):
#     """Login view."""  # sessionMiddleware nos da la propiedad de acceder al request.user
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password) # aqui verifica
#         if user is not None:
#             login(request, user) # aqui hace el login
#             return redirect('posts:feed')
#         else:
#             return render(request, 'users/login.html', {'error': 'Invalid username and password'})
#
#     return render(request, 'users/login.html')




class SignupView(FormView):
    # display a form
    #on error redisplay the form with validations
    #on succes redirects to a new url
    template_name = 'users/signup.html' # template
    form_class = SignupForm # form for that view
    success_url = reverse_lazy('users:login') # redirect

    def form_valid(self, form):
        '''save form data'''
        form.save()  # save form
        return super().form_valid(form)




    # def signup(request): # second ver
    #     # import pdb; pdb.set_trace()
    #     """Sign up view."""
    #     if request.method == 'POST':
    #         form = SignupForm(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             return redirect('users:login')
    #     else:
    #         form = SignupForm()
    #
    #     return render(
    #         request=request,
    #         template_name='users/signup.html',
    #         context={'form': form}
    #     )


    # if request.method == 'POST':
    #     email = request.POST['email']
    #     username = request.POST['username']
    #     passwd = request.POST['passwd']
    #     passwd_confirmation = request.POST['passwd_confirmation']
    #
    #     if passwd != passwd_confirmation:
    #         return render(request, 'users/signup.html', {'error': 'Password confirmation does not match'})
    #
    #
    #     try:
    #         user = User.objects.create_user(username=username, password=passwd)
    #     except IntegrityError:
    #         return render(request, 'users/signup.html', {'error': 'Username is already in user'})
    #
    #     user.first_name = request.POST['first_name']
    #     user.last_name = request.POST['last_name']
    #
    #     user.email = request.POST['email']
    #
    #     if User.objects.filter(email=email):
    #         return render(request, 'users/signup.html', {'error': 'Email is already in used!'})
    #
    #     user.save()
    #
    #     profile = Profile(user=user)
    #     profile.save()
    #
    #     return redirect('users:login')
    #
    # return render(request, 'users/signup.html')


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    ''''logout view'''
    pass


# @login_required
# def logout_view(request):
#     logout(request)
#     return redirect('users:login')
#
