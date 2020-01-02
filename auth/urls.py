from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'auth'),
    path('signin', views.login, name = 'login'),
    path('signup', views.signup, name = 'signup'),
    path('logout', views.logout, name = 'logout'),
    path('', include('django.contrib.auth.urls'))
    #path('password_change', , name = 'password_change')
    #path('', include('django.contrib.auth.urls')),
]