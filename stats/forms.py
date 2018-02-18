from django import forms
from stats.models import analyz


class DocumentForm(forms.ModelForm):
    class Meta:
        model = analyz
        fields = ('upload', )
