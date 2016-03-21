from django import forms

class ContactsForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea,
    )
