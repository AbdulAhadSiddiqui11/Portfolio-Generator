from django.contrib import admin
from .models import Template

admin.site.site_header = "PortFolio Generator"

admin.site.register(Template)
