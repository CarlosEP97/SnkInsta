from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.list_posts,name='index'),

]