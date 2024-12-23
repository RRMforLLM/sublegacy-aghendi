# your_app/management/commands/check_expired_elements.py
from django.core.management.base import BaseCommand
from django.utils import timezone
from aghendi.models import AgendaElement
from datetime import timedelta

class Command(BaseCommand):
    help = 'Deletes or marks expired agenda elements.'

    def handle(self, *args, **kwargs):
        # Get current date and time
        now = timezone.now()

        # Get elements with passed deadlines
        expired_elements = AgendaElement.objects.filter(deadline__lt=now)

        # You can either delete them or mark them as expired
        for element in expired_elements:
            # Option 1: Deleting expired elements
            element.delete()

            # Option 2: Alternatively, you can mark the element as expired
            # element.status = 'expired'  # Assuming you have a status field to mark expired elements
            # element.save()

            self.stdout.write(self.style.SUCCESS(f'Deleted expired element: {element.subject}'))

        self.stdout.write(self.style.SUCCESS('Expired elements cleanup completed.'))