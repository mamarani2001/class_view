from django import forms
from .models import *

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = '__all__'