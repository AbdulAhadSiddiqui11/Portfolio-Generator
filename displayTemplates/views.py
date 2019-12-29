from django.shortcuts import render, redirect
from .models import Template
from django.contrib.auth.models import auth, User
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    templates = Template.objects.all()
    return render(request, 'templates.html', {'templates': templates})

@login_required
def preview(request):
    if request.method == 'POST' :
        val = request.POST['temp_name']
        return render(request, val)
    else:
        return redirect('/templates')