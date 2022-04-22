from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'users'

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('logout',views.logout_view, name = 'logout'),
    path('signup',views.signup, name = 'signup'),
    path('me/profile',views.update_profile, name='update_profile'),
    path('<str:username>', TemplateView.as_view(template_name='users/detail.html'), name='detail'),

]