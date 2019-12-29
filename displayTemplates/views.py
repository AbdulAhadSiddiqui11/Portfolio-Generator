from django.shortcuts import render

def index(request):
    return render(request, 'templates.html')
def t1(request):
    return render(request, 'template1.html')