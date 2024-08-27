from django.urls import path
from . import views


app_name = 'users'

urlpatterns = [
    path('register/', views.register_view, name="register"),
    path('login/', views.login_view, name = "login"),
    path('logout/', views.logout_view, name="logout"),
    path('', views.users_view, name="list"),
    path('<slug:slug>', views.user_page, name = "page")
]
