from django import forms
from product.models import ProductVersionReview

class CommentForm(forms.ModelForm):
     class Meta:
        model = ProductVersionReview
        fields = [
            'full_name',
            'email',
            'comment',
        ]

        widgets = {
            "full_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Your Full Name"
            }),
           
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Your Email"
            }),
           
            "comment": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Comment",
                "cols": 30,
                "rows": 7
            })  
        }