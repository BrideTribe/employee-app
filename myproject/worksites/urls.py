from django.urls import path, include
from . import views

app_name = 'worksites'

urlpatterns = [
    path('', views.posts_list, name='list'),
    path('single-list/', views.posts_user_list, name="single-list"),
    path('new-post/', views.post_new, name= "new-post"),
    path('update-post/', views.post_update, name = "update-post"),
    path('<slug:slug>', views.post_page, name = "page"),
]
