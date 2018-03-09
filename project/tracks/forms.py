from django import forms
from .models import Tracks


class TrackForm(forms.ModelForm):
    class Meta:
        model = Tracks
        fields = ('track_name','audio_file',)
        labels = {
            'audio_file': 'Audio File'
        }

