from django.contrib import admin
from .models import *


class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 0

class UserInfoAdmin(admin.ModelAdmin):
    inlines = [ExperienceInline]

admin.site.register(UserInfo, UserInfoAdmin)