from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator

username_validator = UnicodeUsernameValidator()

'''class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user'''

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=12, min_length=4, required=True, help_text='Required: First Name',
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=12, min_length=4, required=True, help_text='Required: Last Name',
                               widget=(forms.TextInput(attrs={'class': 'form-control'})))
    email = forms.EmailField(max_length=50, help_text='Required. Inform a valid email address.',
                             widget=(forms.TextInput(attrs={'class': 'form-control'})))
    password1 = forms.CharField(label=_('Password'),
                                widget=(forms.PasswordInput(attrs={'class': 'form-control'})),
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label=_('Password Confirmation'), widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                help_text=_('Just Enter the same password, for confirmation'))
    username = forms.CharField(
        label=_('Username'),
        max_length=150,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={'unique': _("A user with that username already exists.")},
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

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


def signup(request):
    '''if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form' : form})'''

    print(request.method)
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password1 = request.POST['password']
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
            return render(request, 'success.html',{'value':'Registration'})
    else:
        return render(request, 'signup.html')

def logout(request):
    auth.logout(request)
    return redirect('/')