from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'users'

urlpatterns = [
    # path('login', views.login_view, name='login'),
    path('login', views.LoginView.as_view(), name='login'),
    # path('logout',views.logout_view, name = 'logout'),
    path('logout',views.LogoutView.as_view(), name = 'logout'),
    # path('signup',views.signup, name = 'signup'),
    path('signup',views.SignupView.as_view(),name='signup'),
    # path('me/profile',views.update_profile, name='update_profile'),
    path('me/profile',views.UpdateProfileView.as_view(), name='update_profile'),
    path('<str:username>', views.UserDetailView.as_view(), name='detail'),
    # path('<str:username>/followers', views.FollowDetailView.as_view(), name='folllow'),
    # path('<str:username>', views.userdetail, name='detail'),
    path('<str:username>/followers/add', views.addfollower, name='addfollower'),
    path('<str:username>/followers/remove', views.removefollower, name='removefollower'),
]