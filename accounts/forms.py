from django import forms
from .models import User, Profile


# =========================
# SIGNUP FORM
# =========================
class SignupForm(forms.ModelForm):
    phone = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Phone Number"})
    )
    nationality = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Nationality"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password"})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password"})
    )

    class Meta:
        model = User
        fields = ["username", "email"]
        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Username"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email Address"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get("password1")
        p2 = cleaned_data.get("password2")

        if p1 and p2 and p1 != p2:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active = True
        user.is_approved = False

        if commit:
            user.save()
            Profile.objects.create(
                user=user,
                phone=self.cleaned_data.get("phone", ""),
                nationality=self.cleaned_data.get("nationality", "")
            )
        return user


# =========================
# PROFILE FORM (IMAGE + PHONE)
# =========================
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image", "phone"]


# =========================
# EMAIL FORM
# =========================
class EmailForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email"]
