from django.shortcuts import render, redirect
from .models import Template
from django.contrib.auth.models import auth, User
from django.contrib.auth.decorators import login_required

def divide_chunks(l, size, k): 
    temp = []
    for i in range(0, size, k):  
        temp.append(l[i:i + k])
    return temp

@login_required
def index(request):
    templates = Template.objects.all()
    size = templates.count()
    template_list = divide_chunks(templates, size, 3)
    return render(request, 'templates.html', {'templates': template_list, 'size':size})

@login_required
def preview(request, temp_name):
    return render(request, temp_name)
