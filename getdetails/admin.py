from django.contrib import admin
from .models import UserInfo,Experience,School,Certificate,Volunteering,Skill,Project,Award,Organisation


class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 0

class SchoolInline(admin.TabularInline):
    model = School
    extra = 0

class CertificateInline(admin.TabularInline):
    model = Certificate
    extra = 0

class VolunteeringInline(admin.TabularInline):
    model = Volunteering
    extra = 0

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 0

class ProjectInline(admin.TabularInline):
    model = Project
    extra = 0

class AwardInline(admin.TabularInline):
    model = Award
    extra = 0

class OrganisationInline(admin.TabularInline):
    model = Organisation
    extra = 0

class UserInfoAdmin(admin.ModelAdmin):
    inlines = [     ExperienceInline,
                    SchoolInline,
                    CertificateInline,
                    VolunteeringInline,
                    SkillInline,
                    ProjectInline,
                    AwardInline,
                    OrganisationInline,
                ]

admin.site.register(UserInfo, UserInfoAdmin)