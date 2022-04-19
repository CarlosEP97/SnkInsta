from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.list_posts,name='feed'),
    path('new',views.create_post, name = 'create_post')

]