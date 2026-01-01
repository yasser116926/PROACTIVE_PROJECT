import requests
from datetime import date
from notam.models import Notam

ICAO_AIRPORTS = ["HKJK", "HKNW", "HKMO"]

NOTAM_SOURCE = "https://aviationweather.gov/api/data/notam"

def import_notams():
    for icao in ICAO_AIRPORTS:
        response = requests.get(
            NOTAM_SOURCE,
            params={
                "ids": icao,
                "format": "json"
            },
            timeout=15
        )

        if response.status_code != 200:
            continue

        data = response.json()

        for item in data:
            text = item.get("text", "")

            Notam.objects.update_or_create(
                airport=icao,
                title=text[:120],
                defaults={
                    "description": text,
                    "date": date.today(),
                    "priority": "medium",
                    "date_expiry": date.today(),  # we’ll improve parsing later
                }
            )
if __name__ == "__main__":
    import_notams()

    print("NOTAM import completed.")

from django.utils import timezone
from datetime import timedelta
from notam.models import Notam

def refresh_if_needed():
    last = Notam.objects.order_by("-updated_at").first()
    if not last or timezone.now() - last.updated_at > timedelta(minutes=30):
        import_notams()
        print("NOTAMs refreshed.")