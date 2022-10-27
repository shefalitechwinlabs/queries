from django import forms
from .models import ExtendUser
from django.contrib.auth.password_validation import validate_password
from django.core import validators

class SignupForm(forms.ModelForm):
   password = forms.CharField(widget = forms.PasswordInput,validators=[validate_password])
   confirm_password = forms.CharField(widget = forms.PasswordInput,validators=[validate_password])
   
   class Meta:
      model = ExtendUser
      fields = ['username', 'first_name', 'last_name', 'email', 'bio_desc', 'password']

   def clean(self):
        cleaned_data = super(SignupForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )    

# class SignupForm(forms.ModelForm):
#    password = forms.CharField(max_length=20, required=True)
#    password_confirm = forms.CharField(max_length=20, required=True)

#    class Meta:
#       model = ExtendUser
#       fields = ['username', 'first_name', 'last_name', 'email', 'bio_desc', 'password']

#       def validate(self):
#          cleaned_data = super(SignupForm, self).clean()
#          password = cleaned_data.get('password_confirm')

#             # if password != password_confirm:
#             #     raise forms.ValidationError('Passwords do not match!')