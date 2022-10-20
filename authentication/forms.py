from django import forms
from .models import Signup

class SignupForm(forms.ModelForm):

   class Meta:
      model = Signup
      fields = ['email','name','bio_desc','image']