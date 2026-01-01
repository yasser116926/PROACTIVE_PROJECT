from django.core.management.base import BaseCommand
from notam.services.notam_importer import import_notams

class Command(BaseCommand):
    help = "Import NOTAMs for Kenyan airports"

    def handle(self, *args, **kwargs):
        import_notams()
        self.stdout.write(self.style.SUCCESS("NOTAMs imported successfully"))
