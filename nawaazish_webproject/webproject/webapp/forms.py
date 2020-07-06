from django import forms
from .models import JoinUs, ContactUs

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'subject', 'message']

        widgets = {
                    'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
                    'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your E-Mail Id'}),
                    'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
                    'message': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Message'}),
                  }


class JoinUsForm(forms.ModelForm):
    class Meta:
        model = JoinUs
        fields = ['name', 'city', 'area', 'pincode', 'phone', 'email', 'insta', ]

        widgets = {
                    'name': forms.TextInput(attrs={'class': 'form-control customInput', 'placeholder': 'Name', 'id': 'username', 'label':''}),
                    'city': forms.TextInput(attrs={'class': 'form-control customInput', 'placeholder': 'City', 'id': 'emailLogIn', 'style':"width:49%; display: inline"}),
                    'area': forms.TextInput(attrs={'class': 'form-control customInput', 'placeholder': 'Area/Locality', 'id': 'emailLogIn', 'style': "width:49%; display: inline"}),
                    'pincode': forms.TextInput(attrs={'class': 'form-control customInput', 'placeholder': 'Pincode', 'id': 'emailLogIn', 'style': "width:49%; display: inline"}),
                    'phone': forms.TextInput(
                                attrs={'class': 'form-control customInput', 'placeholder': 'Contact No.', 'id': 'emailLogIn',
                                       'style': "width:49%; display: inline"}),
                    'email': forms.TextInput(
                                attrs={'class': 'form-control customInput', 'placeholder': 'Email Address', 'id': 'emailLogIn'}),
                    'insta': forms.TextInput(
                                attrs={'class': 'form-control customInput', 'placeholder': 'Instagram handle', 'id': 'passwordLogIn'}),


                 }


