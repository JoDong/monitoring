from django.forms import ModelForm

from domain.models import UrlModel
from statuslog.models import StatusLog


class UrlForm(ModelForm):
    class Meta:
        model = UrlModel
        fields = ['url_name', 'url']


class StatusLogBaseModelForm(ModelForm):
    class Meta:
        model = StatusLog
        fields = '__all__'


class StatusLogCreateForm(StatusLogBaseModelForm):
    pass
