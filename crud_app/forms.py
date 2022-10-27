from django import forms
from .models import *

class EntryForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = "__all__"

class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = "__all__"

