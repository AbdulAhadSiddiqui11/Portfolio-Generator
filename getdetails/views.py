from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from getdetails.models import UserInfo
from django.contrib.auth.decorators import login_required
import json

'''

TODOs

getDetails ->   models -> one to one : user to user info
                ajax -> more tables
                templates -> more templates
                css for get_details
                testing -> unit and integration
                broken links check
                pics and animations

'''


class userInfoForm(forms.ModelForm):

    fname = forms.CharField(max_length = 50)
    lname = forms.CharField(max_length = 50)
    headline = forms.CharField(max_length = 250)
    about = forms.Textarea()
    github = forms.CharField(max_length=150)
    linkedin = forms.CharField(max_length=150)
    email = forms.CharField(max_length=150)
    website = forms.CharField(max_length=150)
    photo = forms.ImageField()
    template_val = forms.CharField(max_length=20)
    
    def __init__(self, user, *args, **kwargs):
        self.user = user
        print(self.user)
        super(userInfoForm, self).__init__(*args, **kwargs)

    class Meta:
        model = UserInfo
        fields = ('fname', 'lname', 'headline', 'about', 'github', 'linkedin','email', 'website', 'photo', 'template_val')
        exclude = ["user"]


# Create your views here.
@login_required
def index(request):
    form = userInfoForm(request.user)
    return render(request, 'details.html', {'form' : form})


@login_required
def addUserPortfolio(request):
    if request.method == 'POST':
        form = userInfoForm(request.user, request.POST, request.FILES)
        #data = json.loads(request.body.decode('utf-8'))
        #print(data)
        user_id = request.user.id
        if form.is_valid() and not UserInfo.objects.filter(user__exact = user_id):
            stock = form.save(commit = False)
            stock.user = request.user
            stock.save()
            return render(request, 'details.html')
        else:
            return redirect('/details')
    else:
        return redirect('/details')


