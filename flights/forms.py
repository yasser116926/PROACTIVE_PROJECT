from django import forms
from .models import Flight

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ["aircraft", "time", "name", "ex"]
        widgets = {
            "aircraft": forms.Select(attrs={"class": "form-control"}),
            "time": forms.TimeInput(attrs={
                "class": "form-control",
                "type": "time"
            }),
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Flight / Crew Name"
            }),
            "ex": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "EX"
            }),
        }
    def clean_time(self):
        time = self.cleaned_data.get("time")
        if not time:
            self.add_error("time", "Time is required.")
        return time