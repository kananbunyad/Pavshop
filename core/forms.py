from django import forms
from core.models import Contact,Newsletter
from django.core.validators import validate_email



class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = [
            'full_name',
            'phone_number',
            'email',
            'subject',
            'message',
        ]
        widgets = {
            "full_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Your Name"
            }),
             "phone_number": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Your Phone Number"
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Your Email"
            }),
            "subject": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Subject"
            }),
            "message": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Message",
                "cols": 30,
                "rows": 7
            })  
        }


    
    # def clean_email(self):
    #     email = self.cleaned_data.get("email")
    #     if not validate_email(email):
    #         raise forms.ValidationError("Enter a valid email address")
    #     return email
    
    def clean_message(self):
        message = self.cleaned_data.get("message")
        if not " " in message:
            raise forms.ValidationError("Enter a valid message")
        return message


    


# class NewsletterForm(forms.ModelForm):
#     email = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'Enter your email address',
#     }))

#     class Meta:
#         model = Newsletter
#         fields = (
#             'email'

#             )



# class NewsletterForm(forms.ModelForm):
#     class Meta:
#         model = Newsletter
#         fields = ['email']
#         widgets = {
#             'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'})
#         }