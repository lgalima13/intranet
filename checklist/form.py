from django import forms
from .models import Check

class CheckForm(forms.ModelForm):
    observacao = forms.CharField(max_length=255)

    class Meta:
        model = Check
        fields = ['observacao']