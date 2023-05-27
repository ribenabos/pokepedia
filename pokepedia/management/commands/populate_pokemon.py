import pokebase as pb
from django.core.management.base import BaseCommand
from pokedex.models import Pokemon

# This will take a while to run, so be patient!


class Command(BaseCommand):
    help = 'Populate or update the database with data from the Pokémon API.'

    def handle(self, *args, **options):
        for pokemon_id in range(1, 899):  # Change the range to populate or update more or less Pokemon
            pokemon_data = pb.pokemon(pokemon_id)
            defaults = {
                'height': pokemon_data.height,
                'weight': pokemon_data.weight,
                'base_experience': pokemon_data.base_experience,
                'is_default': pokemon_data.is_default,
                'order': pokemon_data.order,
                'species': pokemon_data.species.name,
                'sprites': pokemon_data.sprites,
                'forms': pokemon_data.forms,
                'location_area_encounters': pokemon_data.location_area_encounters,
                'abilities': pokemon_data.abilities,
                'moves': pokemon_data.moves,
                'types': pokemon_data.types,
                'stats': pokemon_data.stats,
                'past_types': pokemon_data.past_types,
                'game_indices': pokemon_data.game_indices,
            }

            pokemon, created = Pokemon.objects.update_or_create(
                name=pokemon_data.name,
                defaults=defaults
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created Pokemon: {pokemon.name}'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Successfully updated Pokemon: {pokemon.name}'))
