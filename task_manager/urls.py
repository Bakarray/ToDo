from django.urls import path
from . import views


urlpatterns = [
    path("", views.home_page, name='home_page'),
    path("create_task/", views.create_task, name='create_task')
]