from django import forms
from .models import Contact, Signin, Contactus

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class SigninForm(forms.ModelForm):
    class Meta:
        model = Signin
        fields = '__all__'

class ContactusForm(forms.ModelForm):
    class Meta:
        model = Contactus
        fields = '__all__'