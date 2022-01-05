from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('about-us', views.about, name="about"),
    path('create_task', views.create_task, name="create_task")
]
