from django.db import models

class Tracks(models.Model):
    track_name = models.CharField(max_length=250, blank=False, help_text=("Add a name to your audio file"))
    audio_file = models.FileField(upload_to = 'uploads/%Y/%m/%d/',)
    uploaded_at = models.DateTimeField(auto_now_add=True)
