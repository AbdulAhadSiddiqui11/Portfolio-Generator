from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'templates'),
    path('t1', views.t1, name='t1'),
]