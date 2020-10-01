from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'templates'),
    path('preview/<str:temp_name>', views.preview, name='template'),
]