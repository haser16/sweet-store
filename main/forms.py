from django import forms
from main.models import Contact


class ContactForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Full Name '}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone number'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    text = forms.CharField(widget=forms.TextInput(attrs={'class': 'message-box', 'placeholder': 'Message'}))

    class Meta:
        model = Contact
        fields = ['full_name', 'phone_number', 'email', 'text']
