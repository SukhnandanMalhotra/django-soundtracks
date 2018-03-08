from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, Http404, HttpResponseRedirect,
from .forms.py import TrackForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Tracks


class AllTracksView(ListView):
    model = Tracks
    template_name = 'tracks/all_tracks.html'
    context_object_name = 'audiofiles'

class TrackUploadView(CreateView):
    form_class = TrackForm
    template_name = 'tracks/track_upload.html'

    def form_valid(self, form):
        audio = form.save(commit=False)
        audio.save()
        return  HttpResponseRedirect(reverse('home'))
