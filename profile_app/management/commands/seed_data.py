from django.core.management.base import BaseCommand
from profile_app.models import Profile, Project, Work

class Command(BaseCommand):
    help = 'Seed the database with initial profile, projects, and work'

    def handle(self, *args, **options):
        # Projects
        p1 = Project.objects.create(
            title="Smart Traffic Light System",
            description="Arduino-based traffic controller optimizing signals",
            technologies="arduino,c,embedded",
            links={"github":"https://github.com/geeta/traffic"}
        )
        p2 = Project.objects.create(
            title="EMI Energy Harvesting",
            description="Harvesting ambient EMI for IoT devices",
            technologies="python,electronics",
            links={"github":"https://github.com/geeta/emi"}
        )

        # Work
        w1 = Work.objects.create(
            company="NIT Goa",
            links={"linkedin":"https://linkedin.com/in/geeta"}
        )

        # Profile
        profile = Profile.objects.create(
            name="Geetanjali Saini",
            email="geeta@example.com",
            education="B.Tech Electronics & Communication, NIT Goa",
            bio="Electronics & Communication student passionate about AI, IoT, and automation.",
            skills="arduino,python,c,electronics"
        )
        profile.projects.set([p1, p2])
        profile.work.set([w1])

        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))
