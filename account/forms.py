from typing import Any
from django import forms
from django.contrib.auth import get_user_model,password_validation, authenticate
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm ,SetPasswordForm
from django.utils.translation import gettext_lazy as _



User = get_user_model()



class RegisterForm(UserCreationForm):

    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",'class':'form-control', "placeholder": "Password "}),
        help_text=password_validation.password_validators_help_text_html(),
        max_length=255
        
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'class':'form-control', "placeholder": "Password confirmation"}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )
   
    
    country = CountryField().formfield(widget=CountrySelectWidget(attrs={
        'class': 'form-control', 
        'placeholder': 'Select Country',
    }))

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'phone_number',
            'address',
            'city',
            'country',
            'password1',
            'password2',
          
            
            
        )
        widgets = {
            "first_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Your First Name"
            }),
            "last_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Your Last Name"
            }),
               "username": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Your Userame"
            }),
             "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Your Email Address"
            }),

             "phone_number": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Your Phone Number"
            }),
             "password": forms.PasswordInput(attrs={
                "class": "form-control",
                "placeholder": "Your Password"
            }),
            
            "address": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Address "
            }),

             "city": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Your City"
            }),
            
        }

    
    


    def save(self, commit=True):
        user = super().save(commit=False) 
        user.set_password(self.cleaned_data['password1']) 
        if commit:
            user.save() 
        return user
    

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
    }))

    class Meta:
        fields = (
            'username',
            'password',
        )


class User_EditForm(forms.ModelForm):
    profile_image=forms.ImageField(
        widget = forms.FileInput(
            attrs = {
                "class": "form-control"
                    }
            ))
    old_password = forms.CharField(
        label="Old Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"class": "form-control", "autocomplete": "current-password"}),
        required=False
    )
    new_password1 = forms.CharField(
        label="New Password",
        widget=forms.PasswordInput(attrs={"class": "form-control", "autocomplete": "new-password"}),
        required=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label="New Password Confirmation",
        strip=False,
        widget=forms.PasswordInput(attrs={"class": "form-control", "autocomplete": "new-password"}),
        required=False
    )


    class Meta:
        model = User

        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'profile_image',
            'bio',
            
        ]
        widgets = {
            "first_name": forms.TextInput(attrs={
                "class": "form-control"
                
            }),
             "last_name": forms.TextInput(attrs={
                "class": "form-control"
                
            }),
             "phone_number": forms.TextInput(attrs={
                "class": "form-control"
                
            }),
            
           
            "bio": forms.Textarea(attrs={
                "class": "form-control",
                "cols": 30,
                "rows": 7
            }),

           
        }

    def clean_old_password(self):
            old_password = self.cleaned_data.get("old_password")
            if old_password:
                user = authenticate(username=self.instance.username, password=old_password)
                if user is None:
                    raise forms.ValidationError("Old password is incorrect.")
            return old_password

    def clean(self):
            cleaned_data = super().clean()
            new_password1 = cleaned_data.get("new_password1")
            new_password2 = cleaned_data.get("new_password2")

            if new_password1 and new_password1 != new_password2:
                self.add_error('new_password2', "The two password fields didn’t match.")

            if new_password1:
                password_validation.validate_password(new_password1, self.instance)

    def save(self, commit=True):
            user = super().save(commit=False)
            if self.cleaned_data["new_password1"]:
                user.set_password(self.cleaned_data["new_password1"])
            if commit:
                user.save()
            return user



class ResetForm(forms.Form):

    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",'class':'form-control', "placeholder": "Password "}),
        help_text=password_validation.password_validators_help_text_html(),
        max_length=255
        
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'class':'form-control', "placeholder": "Password confirmation"}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    
   