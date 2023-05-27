from django.db import models
from django.utils.safestring import mark_safe
import pokebase as pb
import json


class Pokemon(models.Model):
    base_experience = models.IntegerField()
    height = models.IntegerField()
    id = models.IntegerField(primary_key=True)
    is_default = models.BooleanField()
    name = models.CharField(max_length=255, unique=True)
    order = models.IntegerField()
    weight = models.IntegerField()
    abilities = models.TextField(default="[]")
    forms = models.TextField(default="[]")
    game_indices = models.TextField(default="[]")
    location_area_encounters = models.TextField(default="[]")
    moves = models.TextField(default="[]")
    past_types = models.TextField(default="[]")
    species = models.TextField(default="[]")
    sprites = models.TextField(default="[]")
    stats = models.TextField(default="[]")
    types = models.TextField(default="[]")

    def __str__(self):
        return self.name

    def get_abilities_as_list(self):
        try:
            return json.loads(self.abilities)
        except json.JSONDecodeError:
            return []

    def get_forms_as_list(self):
        try:
            return json.loads(self.forms)
        except json.JSONDecodeError:
            return []

    def get_game_indices_as_list(self):
        try:
            return json.loads(self.game_indices)
        except json.JSONDecodeError:
            return []

    def get_location_area_encounters_as_list(self):
        try:
            return json.loads(self.location_area_encounters)
        except json.JSONDecodeError:
            return []

    def get_moves_as_list(self):
        try:
            return json.loads(self.moves)
        except json.JSONDecodeError:
            return []

    def display_abilities(self):
        abilities = self.get_abilities_as_list()
        html = '<ul>'
        for ability in abilities:
            html += f'<li><a href="{ability}">{ability}</a></li>'
        html += '</ul>'
        return mark_safe(html)

    def display_forms(self):
        forms = self.get_forms_as_list()
        html = '<ul>'
        for form in forms:
            html += f'<li><a href="{form}">{form}</a></li>'
        html += '</ul>'
        return mark_safe(html)

    def display_game_indices(self):
        game_indices = self.get_game_indices_as_list()
        html = '<ul>'
        for game_index in game_indices:
            html += f'<li><a href="{game_index}">{game_index}</a></li>'
        html += '</ul>'
        return mark_safe(html)

    def display_location_area_encounters(self):
        location_area_encounters = self.get_location_area_encounters_as_list()
        html = '<ul>'
        for location_area_encounter in location_area_encounters:
            html += f'<li><a href="{location_area_encounter}">{location_area_encounter}</a></li>'
        html += '</ul>'
        return mark_safe(html)

    def display_moves(self):
        moves = self.get_moves_as_list()
        html = '<ul>'
        for move in moves:
            html += f'<li><a href="{move}">{move}</a></li>'
        html += '</ul>'
        return mark_safe(html)
