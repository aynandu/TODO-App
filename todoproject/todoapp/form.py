from .models import task
from django import forms

class ToDOForms(forms.ModelForm):
    class Meta:
        model=task
        fields=['name','priority','date']