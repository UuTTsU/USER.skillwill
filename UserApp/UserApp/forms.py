from django import forms

# Create your models here.
class UserFormFields(forms.Form):
    name = forms.CharField(max_length=100),
    last_name = forms.CharField(max_length=100),
    email = forms.EmailField(max_length=100),
    password= forms.CharField(max_length=100)
    age = forms.IntegerField()