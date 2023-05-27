from django.test import TestCase
from django.urls import reverse

from .models import Pokemon


class PokemonModelTest(TestCase):
    def setUp(self):
        self.pokemon = Pokemon.objects.create(
            base_experience=100,
            height=10,
            id=1,
            is_default=True,
            name='Pikachu',
            order=25,
            weight=20,
            abilities='["Ability 1", "Ability 2"]',
            forms='["Form 1", "Form 2"]',
            game_indices='["Index 1", "Index 2"]',
            location_area_encounters='["Location 1", "Location 2"]',
            moves='["Move 1", "Move 2"]',
            past_types=[],
            species=[],
            sprites=[],
            stats=[],
            types=[],
        )

    def test_pokemon_str_representation(self):
        self.assertEqual(str(self.pokemon), 'Pikachu')

    def test_pokemon_display_abilities(self):
        self.assertEqual(self.pokemon.display_abilities(), '<ul><li><a href="Ability 1">Ability 1</a></li><li><a href="Ability 2">Ability 2</a></li></ul>')

    def test_pokemon_display_forms(self):
        self.assertEqual(self.pokemon.display_forms(), '<ul><li><a href="Form 1">Form 1</a></li><li><a href="Form 2">Form 2</a></li></ul>')

    def test_pokemon_display_game_indices(self):
        self.assertEqual(self.pokemon.display_game_indices(), '<ul><li><a href="Index 1">Index 1</a></li><li><a href="Index 2">Index 2</a></li></ul>')

    def test_pokemon_display_location_area_encounters(self):
        self.assertEqual(self.pokemon.display_location_area_encounters(), '<ul><li><a href="Location 1">Location 1</a></li><li><a href="Location 2">Location 2</a></li></ul>')

    def test_pokemon_display_moves(self):
        self.assertEqual(self.pokemon.display_moves(), '<ul><li><a href="Move 1">Move 1</a></li><li><a href="Move 2">Move 2</a></li></ul>')

    def test_pokemon_get_next_by_id(self):
        next_pokemon = self.pokemon.get_next_by_id()
        self.assertIsNone(next_pokemon)

    def test_pokemon_get_previous_by_id(self):
        previous_pokemon = self.pokemon.get_previous_by_id()
        self.assertIsNone(previous_pokemon)

    def test_pokemon_detail_view(self):
        url = reverse('pokemon_detail', kwargs={'pk': self.pokemon.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Pikachu')

    def test_pokemon_list_view(self):
        url = reverse('pokemon_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_pokemon_abilities_as_list(self):
        abilities = self.pokemon.get_abilities_as_list()
        self.assertIsInstance(abilities, list)
        self.assertEqual(abilities, ['Ability 1', 'Ability 2'])

    def test_pokemon_forms_as_list(self):
        forms = self.pokemon.get_forms_as_list()
        self.assertIsInstance(forms, list)
        self.assertEqual(forms, ['Form 1', 'Form 2'])

    def test_pokemon_game_indices_as_list(self):
        game_indices = self.pokemon.get_game_indices_as_list()
        self.assertIsInstance(game_indices, list)
        self.assertEqual(game_indices, ['Index 1', 'Index 2'])

    def test_pokemon_location_area_encounters_as_list(self):
        location_area_encounters = self.pokemon.get_location_area_encounters_as_list()
        self.assertIsInstance(location_area_encounters, list)
        self.assertEqual(location_area_encounters, ['Location 1', 'Location 2'])

    def test_pokemon_moves_as_list(self):
        moves = self.pokemon.get_moves_as_list()
        self.assertIsInstance(moves, list)
        self.assertEqual(moves, ['Move 1', 'Move 2'])

    def test_pokemon_next_by_id(self):
        next_pokemon = Pokemon.objects.create(
            base_experience=200,
            height=20,
            id=2,
            is_default=True,
            name='Raichu',
            order=30,
            weight=25,
            abilities='["Ability 3", "Ability 4"]',
            forms=[],
            game_indices=[],
            location_area_encounters=[],
            moves=[],
            past_types=[],
            species=[],
            sprites=[],
            stats=[],
            types=[],
        )
        self.assertEqual(self.pokemon.get_next_by_id(), next_pokemon)

    def test_pokemon_previous_by_id(self):
        previous_pokemon = Pokemon.objects.create(
            base_experience=50,
            height=5,
            id=0,
            is_default=True,
            name='Pichu',
            order=20,
            weight=10,
            abilities=[],
            forms=[],
            game_indices=[],
            location_area_encounters=[],
            moves=[],
            past_types=[],
            species=[],
            sprites=[],
            stats=[],
            types=[],
        )
        self.assertEqual(self.pokemon.get_previous_by_id(), previous_pokemon)
