from django import forms
from .models import FeedBack

class FeedBackForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "name",
                "placeholder": "Full Name"
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "id": "email",
                "placeholder": "E-Mail Address"
            }
        )
    )
    subject = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "subject",
                "placeholder": "Subject"
            }
        )
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "id": "message",
                "placeholder": "Your Message"
            }
        )
    )

    def clean(self):
        has_errors = False
        if len(self.cleaned_data["message"]) > 40:
            self.add_error("message","A lot of size")
            has_errors = True
        if self.cleaned_data["subject"].lower() == "google":
            self.add_error("subject","Really?")
            has_errors = True

        if has_errors:
            print("invalid")
            raise forms.ValidationError('Invalid form')
        return self.cleaned_data

    def save(self):
        FeedBack.objects.create(**self.cleaned_data)