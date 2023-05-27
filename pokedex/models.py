from django.db import models
from django.utils.safestring import mark_safe
import json

from rest_framework.fields import JSONField


class Pokemon(models.Model):
    base_experience = models.IntegerField()
    height = models.IntegerField()
    id = models.IntegerField(primary_key=True)
    is_default = models.BooleanField()
    name = models.CharField(max_length=255, unique=True)
    order = models.IntegerField()
    weight = models.IntegerField()
    abilities = JSONField(default=list)
    forms = JSONField(default=list)
    game_indices = JSONField(default=list)
    location_area_encounters = JSONField(default=list)
    moves = JSONField(default=list)
    past_types = JSONField(default=list)
    species = JSONField(default=list)
    sprites = JSONField(default=list)
    stats = JSONField(default=list)
    types = JSONField(default=list)

    def __init__(self, *args, **kwargs):
        abilities = kwargs.pop('abilities', [])
        forms = kwargs.pop('forms', [])
        game_indices = kwargs.pop('game_indices', [])
        location_area_encounters = kwargs.pop('location_area_encounters', [])
        moves = kwargs.pop('moves', [])
        super().__init__(*args, **kwargs)
        self.abilities = abilities
        self.forms = forms
        self.game_indices = game_indices
        self.location_area_encounters = location_area_encounters
        self.moves = moves

    def __str__(self):
        return self.name

    def get_abilities_as_list(self):
        abilities = self.abilities
        return json.loads(abilities) if isinstance(abilities, str) else []

    def get_forms_as_list(self):
        forms = self.forms
        return json.loads(forms) if isinstance(forms, str) else []

    def get_game_indices_as_list(self):
        game_indices = self.game_indices
        return json.loads(game_indices) if isinstance(game_indices, str) else []

    def get_location_area_encounters_as_list(self):
        location_area_encounters = self.location_area_encounters
        return json.loads(location_area_encounters) if isinstance(location_area_encounters, str) else []

    def get_moves_as_list(self):
        moves = self.moves
        return json.loads(moves) if isinstance(moves, str) else []

    def get_species_as_list(self):
        species = self.species
        return json.loads(species) if isinstance(species, str) else []

    def get_sprites_as_list(self):
        sprites = self.sprites
        return json.loads(sprites) if isinstance(sprites, str) else []

    def get_stats_as_list(self):
        stats = self.stats
        return json.loads(stats) if isinstance(stats, str) else []

    def get_types_as_list(self):
        types = self.types
        return json.loads(types) if isinstance(types, str) else []

    def display_abilities(self):
        abilities = self.get_abilities_as_list()
        html = '<ul>'
        if abilities:
            for ability in abilities:
                html += f'<li><a href="{ability}">{ability}</a></li>'
        else:
            html += '<li>No abilities</li>'
        html += '</ul>'
        return mark_safe(html)

    def display_forms(self):
        forms = self.get_forms_as_list()
        html = '<ul>'
        if forms:
            for form in forms:
                html += f'<li><a href="{form}">{form}</a></li>'
        else:
            html += '<li>No forms</li>'
        html += '</ul>'
        return mark_safe(html)

    def display_game_indices(self):
        game_indices = self.get_game_indices_as_list()
        html = '<ul>'
        if game_indices:
            for game_index in game_indices:
                html += f'<li><a href="{game_index}">{game_index}</a></li>'
        else:
            html += '<li>No game indices</li>'
        html += '</ul>'
        return mark_safe(html)

    def display_location_area_encounters(self):
        location_area_encounters = self.get_location_area_encounters_as_list()
        html = '<ul>'
        if location_area_encounters:
            for location_area_encounter in location_area_encounters:
                html += f'<li><a href="{location_area_encounter}">{location_area_encounter}</a></li>'
        else:
            html += '<li>No location area encounters</li>'
        html += '</ul>'
        return mark_safe(html)

    def display_moves(self):
        moves = self.get_moves_as_list()
        html = '<ul>'
        if moves:
            for move in moves:
                html += f'<li><a href="{move}">{move}</a></li>'
        else:
            html += '<li>No moves</li>'
        html += '</ul>'
        return mark_safe(html)

    def display_species(self):
        species = self.get_species_as_list()
        html = '<ul>'
        if species:
            for specie in species:
                html += f'<li><a href="{specie}">{specie}</a></li>'
        else:
            html += '<li>No species</li>'
        html += '</ul>'
        return mark_safe(html)

    def display_sprites(self):
        sprites = self.get_sprites_as_list()
        html = '<ul>'
        if sprites:
            for sprite in sprites:
                html += f'<li><a href="{sprite}">{sprite}</a></li>'
        else:
            html += '<li>No sprites</li>'
        html += '</ul>'
        return mark_safe(html)

    def display_stats(self):
        stats = self.get_stats_as_list()
        html = '<ul>'
        if stats:
            for stat in stats:
                html += f'<li><a href="{stat}">{stat}</a></li>'
        else:
            html += '<li>No stats</li>'
        html += '</ul>'
        return mark_safe(html)

    def display_types(self):
        types = self.get_types_as_list()
        html = '<ul>'
        if types:
            for type in types:
                html += f'<li><a href="{type}">{type}</a></li>'
        else:
            html += '<li>No types</li>'
        html += '</ul>'
        return mark_safe(html)

    def get_next_by_id(self):
        try:
            return Pokemon.objects.filter(id__gt=self.id).order_by('id').first()
        except Pokemon.DoesNotExist:
            return None

    def get_previous_by_id(self):
        try:
            return Pokemon.objects.filter(id__lt=self.id).order_by('-id').first()
        except Pokemon.DoesNotExist:
            return None
