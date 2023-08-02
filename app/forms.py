from django import forms
from app.models import *
class studentform(forms.ModelForm):
    class Meta:
        model=student 
        fields='__all__'
