from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'templates'),
    path('preview', views.preview, name='template'),
]