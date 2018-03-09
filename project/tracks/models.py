from django.db import models
from .validators import validate_file_type


class Tracks(models.Model):
    track_name = models.CharField(max_length=250, blank=False,)
    audio_file = models.FileField(upload_to='uploads/%Y/%m/%d/', validators=[validate_file_type])
    uploaded_at = models.DateTimeField(auto_now_add=True)
