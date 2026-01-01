from django import forms
from .models import Event
from django.utils import timezone



class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'title',
            'description',
            'date',
            'time',
            'location',
        ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
        }
    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date and date < timezone.now().date():
            self.add_error('date', 'Event date cannot be in the past.')
        return date
        
    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')

        if date == timezone.now().date() and time and time < timezone.now().time():
            self.add_error('time', 'Event time cannot be in the past for today\'s date.')

        return cleaned_data