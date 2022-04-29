from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostsFeedView.as_view(),name='feed'),
    # path('new',views.create_post, name = 'create_post'),
    path('new',views.CreatePostView.as_view(), name = 'create_post'),
    path('<int:pk>',views.PostDetailView.as_view(),name='detail'),

]