from django.db import models


class Ability(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Form(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class GameIndex(models.Model):
    index = models.IntegerField()
    game = models.CharField(max_length=255)

    def __str__(self):
        return f"Game: {self.game}, Index: {self.index}"


class LocationArea(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Move(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Stat(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Pokemon(models.Model):
    abilities = models.ManyToManyField(Ability)
    base_experience = models.IntegerField()
    forms = models.ForeignKey(Form, on_delete=models.CASCADE)
    game_indices = models.ManyToManyField(GameIndex)
    height = models.IntegerField()
    id = models.IntegerField(primary_key=True)
    is_default = models.BooleanField()
    location_area_encounters = models.ForeignKey(LocationArea, on_delete=models.CASCADE)
    moves = models.ManyToManyField(Move)
    name = models.CharField(max_length=255, unique=True)
    order = models.IntegerField()
    past_types = models.ManyToManyField(Type, related_name='past_pokemon')
    species = models.OneToOneField(Type, on_delete=models.CASCADE, related_name='pokemon')
    sprites = models.OneToOneField(Type, on_delete=models.CASCADE, related_name='pokemon_sprites')
    stats = models.ManyToManyField(Stat)
    types = models.ManyToManyField(Type)
    weight = models.IntegerField()

    def __str__(self):
        return self.name
