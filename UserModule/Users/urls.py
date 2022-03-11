from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('recovery', views.recovery, name='recovery'),
    path('verify', views.verify, name='verify'),
]