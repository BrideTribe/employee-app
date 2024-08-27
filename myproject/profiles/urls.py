from django.urls import path
from . import views


app_name = 'profiles'



urlpatterns = [
    path('profile/<str:pk>/', views.profile, name="profile"),
    path('profile_edit/', views.profile_edit, name="profile_edit"),
]