from django import forms
from .models import SchoolClass


class ClassForm(forms.ModelForm):

    class Meta:
        model = SchoolClass
        fields = [
            'subject',
            'instructor',
            'class_room',
            'date',
            'start_time',
            'end_time',
        ]

        widgets = {
            'subject': forms.Select(attrs={'class': 'form-control'}),
            'instructor': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Instructor name'}
            ),
            'class_room': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
            ),
            'start_time': forms.TimeInput(
                attrs={'type': 'time', 'class': 'form-control'}
            ),
            'end_time': forms.TimeInput(
                attrs={'type': 'time', 'class': 'form-control'}
            ),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')

        if start_time and end_time and start_time >= end_time:
            self.add_error('end_time', 'End time must be after start time.')

        return cleaned_data
