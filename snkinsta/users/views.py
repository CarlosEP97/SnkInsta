 # Create your views here.

"""Users views."""

# Django
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required # The login_required decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

#Django Models
from django.contrib.auth.models import User #ModelUser
from posts.models import Post

#Django exceptions
from django.db.utils import IntegrityError

# Forms
from .forms import ProfileForm,SignupForm


class UserDetailView(LoginRequiredMixin,DetailView):
    ''''user detailview'''
    template_name = 'users/detail.html' # recibe el template
    slug_field = 'username' # the name of the field on the model that contains the slug. By default, slug_field is 'slug'.
    #slug execute the queryset for find a user with that username.
    slug_url_kwarg = 'username' # The name of the URLConf keyword argument that contains the slug. By default, slug_url_kwarg is 'slug'.
    queryset = User.objects.all() # The model that this view will display data for. ia specifying queryset
    #A QuerySet that represents the objects. If provided, the value of queryset supersedes the value provided for model.
    context_object_name = 'user' # Designates the name of the variable to use in the context.,Model name in template

    def get_context_data(self, **kwargs):
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




@login_required
def update_profile(request):
        """Update a user's profile view."""
        profile = request.user.profile # sessionMiddleware nos da la propiedad de acceder al request.user


        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES) # Mandar diccionario de POST al formulario , es una instancia y va a tomar los datos de nuestro request
            #se inicializa y se llena con los datos del POST.request
            if form.is_valid():
                data = form.cleaned_data
                print(form.cleaned_data)

                profile.website = data['website']
                profile.phone_number = data['phone_number']
                profile.biography = data['biography']
                profile.picture = data['picture']
                profile.save()

                # url = reverse('users:detail', kwargs ={'username': request.user.username})
                # return redirect(url) # redirect no puede construir la URl como reverse
                return HttpResponseRedirect(reverse('users:detail', kwargs ={'username': request.user.username}))
        else:                                                       # args = (request.user.username,)
            form = ProfileForm()

        return render(
            request=request,
            template_name='users/update_profile.html',
            context={
                'profile': profile,
                'user': request.user,
                'form': form
            }
        )


def login_view(request):
    """Login view."""  # sessionMiddleware nos da la propiedad de acceder al request.user
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password) # aqui verifica
        if user is not None:
            login(request, user) # aqui hace el login
            return redirect('posts:feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})

    return render(request, 'users/login.html')

def signup(request):
    # import pdb; pdb.set_trace()
    """Sign up view."""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = SignupForm()

    return render(
        request=request,
        template_name='users/signup.html',
        context={'form': form}
    )

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



@login_required
def logout_view(request):
    logout(request)
    return redirect('users:login')

