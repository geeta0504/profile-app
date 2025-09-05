from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=200, blank=True, help_text="Comma separated skills")
    links = models.JSONField(default=dict)  # {"github": "...", "portfolio": "..."}

    def __str__(self):
        return self.title

class Work(models.Model):
    company = models.CharField(max_length=100)
    links = models.JSONField(default=dict)  # {"github": "...", "linkedin": "...", "portfolio": "..."}

    def __str__(self):
        return self.company

class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    education = models.TextField(blank=True)
    bio = models.TextField(blank=True)
    skills = models.TextField(blank=True, help_text="Comma separated skills")
    projects = models.ManyToManyField(Project, blank=True, related_name="profiles")
    work = models.ManyToManyField(Work, blank=True, related_name="profiles")

    def __str__(self):
        return self.name
