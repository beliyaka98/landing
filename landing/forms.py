from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'age', 'city', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'fname'}),
            'age': forms.TextInput(attrs={'class': 'form-control', 'id': 'lname'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'id': 'email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'id': 'phone'}),
        }
