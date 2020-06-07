from django.core.management.base import BaseCommand
import re

from locations.models import Country


class Command(BaseCommand):
    help = 'Display list of countries with occurrence'

    def add_arguments(self, parser):
        parser.add_argument('entry_name', type=str, help='Part of the country')

    def handle(self, *args, **kwargs):
        total = kwargs['entry_name']
        country = Country.objects.all()
        for i in range(len(country)):
            match = re.search(total, country[i].name)
            if match:
                self.stdout.write(self.style.SUCCESS(country[i].name + ' - True'))
            else:
                self.stdout.write(self.style.NOTICE(country[i].name + ' - False'))
