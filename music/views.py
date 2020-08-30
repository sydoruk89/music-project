from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Music
from django.urls import reverse_lazy

class MusicListView(ListView):
    template_name = "home.html"
    model = Music

class MusicDetailView(DetailView):
    template_name = "detail.html"
    model = Music

class MusicCreateView(CreateView): 
    template_name = "create.html"
    model = Music
    fields = "__all__"

class MusicUpdateView(UpdateView):
    template_name = "update.html"
    model = Music
    fields = "__all__"

class MusicDeleteView(DeleteView):
    template_name = "delete.html"
    model = Music
    success_url = reverse_lazy('home')