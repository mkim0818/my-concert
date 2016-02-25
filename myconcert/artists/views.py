from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.detail import SingleObjectMixin
from myconcert.artists.models import Artist

class ArtistList(ListView):
    model = Artist
    context_object_name = 'artist-list'

class ArtistDetail(DetailView):
    model = Artist
    context_object_name = 'artist-detail'
