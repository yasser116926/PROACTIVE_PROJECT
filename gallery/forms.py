from django import forms
from .models import GalleryImage



class ImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ["image", "description"]
        widgets = {
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Image description"
            }),
        }


    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if image.size > 5 * 1024 * 1024:  # 5MB limit
                self.add_error('image', 'Image file too large (maximum 5MB).')
            if not image.content_type in ['image/jpeg', 'image/png']:
                self.add_error('image', 'Unsupported file type. Only JPEG and PNG are allowed.')
        return image

    def clean(self):
        cleaned_data = super().clean()
        # Additional cross-field validation can be added here if needed
        return cleaned_data

