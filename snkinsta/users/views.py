 # Create your views here.

"""Users views."""

# Django
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required # The login_required decorator
#Django Models
from django.contrib.auth.models import User #ModelUser
from .models import Profile
#Django exceptions
from django.db.utils import IntegrityError
# Forms
from .forms import ProfileForm,SignupForm

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

                return redirect('users:update_profile')

        else:
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

