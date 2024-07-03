from django import forms
from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30,label="First Name")
    last_name = forms.CharField(max_length=30,label="Last Name")
    phone = forms.CharField(max_length=30,label="Phone")
    cnic = forms.CharField(max_length=30,label="CNIC")

    def save(self, request):
        user = super(CustomSignupForm,self).save(request)
        user.phone = self.cleaned_data['phone']
        user.cnic = self.cleaned_data['cnic']
        user.save()
        return user

