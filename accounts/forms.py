from django import forms
from .models import User


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "password"]

    password = forms.CharField(widget=forms.PasswordInput)


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.is_active = False
        user.is_approved = False
        if commit:
            user.save()
        return user


