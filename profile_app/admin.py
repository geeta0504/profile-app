# profile_app/admin.py
from django.contrib import admin
from .models import Profile, Project, Work

admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Work)
