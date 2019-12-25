from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'auth'),
    path('signin', views.login, name = 'login'),
    path('signup', views.signup, name = 'signup'),
]