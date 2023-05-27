from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
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
        return render(request, 'pokedex_index.html')


class PokemonListView(View):
    def get(self, request):
        pokemon_list = Pokemon.objects.all()
        context = {
            'pokemon_list': pokemon_list
        }

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            # AJAX request, return JSON response
            data = {
                'pokemon_list': [{'pk': pokemon.id, 'name': pokemon.name} for pokemon in pokemon_list]
            }
            return JsonResponse(data)
        else:
            # Regular request, render HTML template
            return render(request, 'pokemon_list.html', context)
