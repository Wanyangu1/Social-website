from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    path('users/', views.user_list, name='user_list'),
    path('users/<username>/', views.user_detail, name='user_detail'),
    path('users/follow/', views.user_follow, name='user_follow'),
]