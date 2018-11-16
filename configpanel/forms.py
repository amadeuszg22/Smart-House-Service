from django import forms
from .models import configweather,configdev


class channelform(forms.ModelForm):

    class Meta:
        model = configweather
        fields = ('web', 'country', 'city', 'cityg')

class devform(forms.ModelForm):

    class Meta:
        model = configdev
        fields = ('name', 'location', 'type', 'model', 'ip')
