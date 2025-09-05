from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from collections import Counter

from .models import Profile, Project, Work
from .serializers import ProfileSerializer, ProjectSerializer, WorkSerializer

# CRUD for profiles
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# CRUD for projects
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

# Health endpoint
@api_view(['GET'])
def health(request):
    return Response({"status": "ok"}, status=200)

# Projects by skill
@api_view(['GET'])
def projects_by_skill(request):
    skill = request.GET.get('skill')
    if not skill:
        return Response({"detail": "provide ?skill=..."}, status=400)
    projects = Project.objects.filter(
        Q(technologies__icontains=skill) |
        Q(title__icontains=skill) |
        Q(description__icontains=skill)
    ).distinct()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)

# Top 10 skills
@api_view(['GET'])
def top_skills(request):
    skills_list = []
    for p in Profile.objects.all():
        if p.skills:
            skills_list += [s.strip().lower() for s in p.skills.split(',')]
    top = Counter(skills_list).most_common(10)
    return Response({"top_skills": top})

# Search endpoint
@api_view(['GET'])
def search(request):
    q = request.GET.get('q', '')
    if not q:
        return Response([], status=200)
    profiles = Profile.objects.filter(
        Q(name__icontains=q) |
        Q(email__icontains=q) |
        Q(bio__icontains=q) |
        Q(skills__icontains=q)
    )
    projects = Project.objects.filter(
        Q(title__icontains=q) |
        Q(description__icontains=q) |
        Q(technologies__icontains=q)
    )
    return Response({
        "profiles": ProfileSerializer(profiles, many=True).data,
        "projects": ProjectSerializer(projects, many=True).data,
    })
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Profile App API")
