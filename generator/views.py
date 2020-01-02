from django.shortcuts import render
from getdetails.models import UserInfo,Experience,School,Certificate
from getdetails.models import Volunteering,Skill,Project,Award,Organisation
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    user_id = request.user.id                                                               # Using user_id because foreign key is mapped to primary key of user i.e. user_id not username (request.user)
    if not UserInfo.objects.filter(user__exact = user_id):                                  # If the query set doesn't have a single element
       return render(request, 'failure_portfolio.html', {'value':request.user})
    else:
        user_bio_id = UserInfo.objects.filter(user__exact = user_id).get().id               # get() returns a single element instead of a query set
        user_bio = UserInfo.objects.filter(user__exact = user_id).get()
        experiences = Experience.objects.filter(userinfo__exact = user_bio_id)
        schools = School.objects.filter(userinfo__exact = user_bio_id)
        certificates = Certificate.objects.filter(userinfo__exact = user_bio_id)
        volunteerings = Volunteering.objects.filter(userinfo__exact = user_bio_id)
        skills = Skill.objects.filter(userinfo__exact = user_bio_id)
        projects = Project.objects.filter(userinfo__exact = user_bio_id)
        awards = Award.objects.filter(userinfo__exact = user_bio_id)
        orgs = Organisation.objects.filter(userinfo__exact = user_bio_id)
        print(experiences)
        return render(request, user_bio.template_val, {'value' : 'portfolio',
                                                        'bio' : user_bio,
                                                        'exp': experiences,
                                                        'schools':schools,
                                                        'certificates':certificates,
                                                        'vols':volunteerings,
                                                        'skills':skills,
                                                        'projects':projects,
                                                        'awards':awards,
                                                        'orgs':orgs})




