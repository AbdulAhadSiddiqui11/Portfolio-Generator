from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name = 'details'),
     path('addportfolio', views.addUserPortfolio, name = 'add user portfolio')
]