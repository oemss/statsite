from django import forms
from stats.models import Stat


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Stat
        fields = ('upload',)