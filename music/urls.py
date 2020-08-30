
from django.urls import path
from .views import MusicListView, MusicDetailView, MusicCreateView, MusicUpdateView, MusicDeleteView

urlpatterns = [
    path('', MusicListView.as_view(), name='home'),
    path('detail/<int:pk>/', MusicDetailView.as_view(), name='detail'),
    path('new/', MusicCreateView.as_view(), name='create'),
    path('detail/<int:pk>/edit/', MusicUpdateView.as_view(), name='update'),
    path('detail/<int:pk>/delete/', MusicDeleteView.as_view(), name='delete')
]