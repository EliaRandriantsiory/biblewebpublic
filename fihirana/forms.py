from django import forms
from .models import fhrn_mod

class Mod_Fihrn(forms.ModelForm):
    class Meta:
        model = fhrn_mod
        fields = ['fhrn_mod']
        widgets = {
            'fhrn_mod': forms.Textarea(attrs={'cols': 80, 'rows':20})  # Spécifiez les attributs pour le champ TextArea
        }