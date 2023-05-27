from django.shortcuts import render
from django.views import View
from .models import Pokemon


class PokemonDetailView(View):
    def get(self, request, pk):
        try:
            pokemon = Pokemon.objects.get(pk=pk)
        except Pokemon.DoesNotExist:
            return render(request, 'pokemon_not_found.html')

        context = {
            'pokemon': pokemon
        }
        return render(request, 'pokemon_detail.html', context)


class PokemonIndexView(View):
    def get(self, request):
        pokemon_list = Pokemon.objects.all()
        context = {
            'pokemon_list': pokemon_list
        }
        return render(request, 'index.html', context)


class PokemonListView(View):
    def get(self, request):
        pokemon_list = Pokemon.objects.all()
        context = {
            'pokemon_list': pokemon_list
        }
        return render(request, 'pokemon_list.html', context)


class PokemonCreateView(View):
    def get(self, request):
        return render(request, 'pokemon_create.html')

    def post(self, request):
        return render(request, 'pokemon_create.html')
