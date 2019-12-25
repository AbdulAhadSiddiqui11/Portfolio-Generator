from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'auth.html')

def login(request):
    print('REQQQQQQQQEEEEEEEEESSSSSSSTTTT     ' ,request.method)
    if request.method == 'POST':
        print('afjdsfodsijfoaidf oadjfoi;adsjfoai oarfoalshd fodashf vnpoa;slih fawpoelf pao')
        username = request.POST['username']
        print(username)
        return render(request, 'success.html/', {'value' : 'Login'})
    else :
        return render(request, 'signin.html')

def signup(request):
    print(request.method)
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        print(username,firstname,lastname,email,password)
        return render(request, 'success.html', {'value' : ' Registration'})
    else:
        return render(request, 'signup.html')