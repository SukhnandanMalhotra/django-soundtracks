from django.urls import re_path

from .views import AllTracksView,TrackUploadView

urlpatterns = [
re_path(r'^all/$',AllTracksView.as_view(),name='home'),
re_path(r'^uploads/form/$',TrackUploadView.as_view(),name='audio-form-upload'),

]
