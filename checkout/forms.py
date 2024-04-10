from django import forms
from checkout.models import BillingAddress

class BillingForm(forms.ModelForm):
     class Meta:
        model = BillingAddress
        fields = [
            'first_name',
            'last_name',
            'company_name',
            'address',
            'city',
            'country',
            'email',
            'phone_number',
        ]

        widgets = {
            "first_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Your First Name"
            }),
             "last_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Your Last Name"
            }),
            "company_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Your Company Name"
            }),
            "address": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Address"
            }),
            "city": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "City"
            }),
           
            "country": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Country"
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Your Email"
            }),
           
           "phone_number": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Phone"
            }),
        }
