from django import forms

from domain.models import UrlModel


class UrlForm(forms.ModelForm):
    class Meta:
        model = UrlModel
        fields = ['url_name', 'url']