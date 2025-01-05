from django.urls import path
from . import views


urlpatterns = [
    path("", views.home_page, name='home_page'),
    path("login/", views.user_login, name='login'),
    path("signup/", views.user_signup, name='signup'),
    path("logout/", views.user_logout, name='logout'),
    path("<int:task_id>/", views.description, name='task_desc'),
    path("create_task/", views.create_task, name='create_task'),
]