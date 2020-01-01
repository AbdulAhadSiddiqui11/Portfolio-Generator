from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Create your views here.

def index(request):
    return render(request, 'auth.html')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect("/")
    else:
        form = AuthenticationForm()
        return render(request, 'signin.html', {'form' : form})
    '''if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            #return render(request, 'success.html/', {'value' : 'Login'})
            return redirect("/")
        else :
            messages.info(request, 'Username or Password Incorrect...')
            return redirect('login')
    else :
        return render(request, 'signin.html')'''

def signup(request):
    print(request.method)
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password1 = request.POST['password1']
        print(username,firstname,lastname,email,password1)
        
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username not available...')
            return redirect('signup')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email already Registered...')
            return redirect('signup')
        else:
            user = User.objects.create_user(username=username, password=password1, email=email, first_name=firstname, last_name=lastname)
            user.save()
            print("User Created")
            #return redirect('signin')
            #return render(request, 'signin.html')
            return render(request, 'success.html', {'value' : ' Registration'})
    else:
        return render(request, 'signup.html')

def logout(request):
    auth.logout(request)
    return redirect('/')