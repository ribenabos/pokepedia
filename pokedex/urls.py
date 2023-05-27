from django.urls import path
from django.views.generic import RedirectView

from .views import *

urlpatterns = [
    path('pokemon/list/<int:pk>/', PokemonDetailView.as_view(), name='pokemon_detail'),
    path('', PokemonIndexView.as_view(), name='pokedex_index'),
    path('pokemon/list/', PokemonListView.as_view(), name='pokemon_list'),
    path('favicon.ico', RedirectView.as_view(url='/static/images/favicon.ico')),
]
