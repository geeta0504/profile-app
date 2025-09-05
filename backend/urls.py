from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profile_app.views import (
    ProfileViewSet,
    ProjectViewSet,
    health,
    projects_by_skill,
    top_skills,
    search
)

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet, basename='profile')
router.register(r'projects', ProjectViewSet, basename='project')

from profile_app.views import home

urlpatterns = [
    path('', home),  # this handles '/'
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/health/', health),
    path('api/projects-by-skill/', projects_by_skill),
    path('api/search/', search),
    path('api/skills/top/', top_skills),
]

