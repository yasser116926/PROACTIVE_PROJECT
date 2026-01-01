from django import forms
from .models import LibraryResource


class LibraryResourceForm(forms.ModelForm):
    class Meta:
        model = LibraryResource
        fields = [
            'subject',
            'book_pdf',
            'question_bank_pdf',
            'formulas_text',
            'diagrams_images',
            'external_links',
        ]

        widgets = {
            'subject': forms.Select(attrs={'class': 'form-control'}),
            'formulas_text': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 5}
            ),
            'external_links': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3}
            ),
        }
    def clean_external_links(self):
        links = self.cleaned_data.get('external_links', '')
        if links:
            link_list = links.splitlines()
            for link in link_list:
                if not (link.startswith('http://') or link.startswith('https://')):
                    self.add_error('external_links', 'Each link must start with http:// or https://')
        return links

    def clean(self):
        cleaned_data = super().clean()
        # Additional cross-field validation can be added here if needed
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        # Any additional processing before saving can be done here
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Custom initialization if needed 
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = f'Enter {field.label}'
        self.fields['subject'].widget.attrs['class'] = 'form-select'
        self.fields['external_links'].help_text = 'Enter one link per line, starting with http:// or https://'  
        self.fields['book_pdf'].required = False
        self.fields['question_bank_pdf'].required = False
        self.fields['diagrams_images'].required = False
        self.fields['formulas_text'].required = False
        self.fields['external_links'].required = False

# from django.contrib.auth.decorators import login_required, user_passes_test        

