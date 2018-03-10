from django.db import models
from .validators import validate_file_extension


class Tracks(models.Model):
    track_name = models.CharField(max_length=250, blank=True)
    audio_file = models.FileField(upload_to='uploads/%Y/%m/%d/', validators=[validate_file_extension])
    uploaded_at = models.DateTimeField(auto_now_add=True)
