from django.core.management.base import BaseCommand
from authentication.models import ExtendUser, Profile
from django.db.models import Count

class Command(BaseCommand):
    help = "Displays stats related to Author's entries"

    def handle(self, *args, **kwargs):
        users = ExtendUser.objects.all().count()
        profile = Profile.objects.all().count()
        print('Number of Users',users)
        print('Number of Profiles',profile)