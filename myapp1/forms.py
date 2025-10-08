# myapp1/forms.py
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'address', 'profession', 'tel_number', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full name'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Address (optional)'}),
            'profession': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Profession (optional)'}),
            'tel_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone (optional)'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'someone@example.com'}),
        }
