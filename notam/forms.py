from django import forms
from .models import Notam
from django.utils import timezone

class NotamForm(forms.ModelForm):
    class Meta:
        model = Notam
        fields = [
            'airport',
            'title',
            'description',
            'date',
            'time',
            'priority',
            'date_expiry',
        ]
        widgets = {
            'airport': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ICAO Code e.g. HKJK'
            }),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'date_expiry': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date < timezone.now().date():
            raise forms.ValidationError("Date cannot be in the past.")
        return date

    def clean_date_expiry(self):
        expiry = self.cleaned_data.get('date_expiry')
        if expiry < timezone.now().date():
            raise forms.ValidationError("Expiry date cannot be in the past.")
        return expiry
