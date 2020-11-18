from django.urls import path

from .import views

urlpatterns = [
  path('', views.dashboard, name='dashboard'),
  path('register/', views.register, name='register'),
  path('edit/', views.edit, name='edit'),
  path('users/', views.user_list, name='user_list'),
  path('users/follow/', views.user_follow, name='user_follow'),
  path('users/<username>/', views.user_detail, name='user_detail'),
]