from django.urls import path
from .views import *

urlpatterns = [
    path('pokemon/<int:pk>/', PokemonDetailView.as_view(), name='pokemon_detail'),
    path('', PokemonIndexView.as_view(), name='pokedex_index'),
    path('pokemon/list/', PokemonListView.as_view(), name='pokemon_list'),
]
