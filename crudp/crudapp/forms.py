from django import forms
from . import models

class EmployeerForm(forms.ModelForm):
    class Meta:
        model = models.Employeer
        fields = '__all__'

        