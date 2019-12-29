from django.shortcuts import render, redirect
from .models import Template

def index(request):
    templates = Template.objects.all()
    return render(request, 'templates.html', {'templates': templates})


def preview(request):
    if request.method == 'POST' :
        val = request.POST['temp_name']
        return render(request, val)
    else:
        return redirect('/templates')