# Generated by Django 4.2.1 on 2023-05-27 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='GameIndex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('game', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='LocationArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Move',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('base_experience', models.IntegerField()),
                ('height', models.IntegerField()),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('is_default', models.BooleanField()),
                ('name', models.CharField(max_length=255, unique=True)),
                ('order', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('abilities', models.ManyToManyField(to='pokedex.ability')),
                ('forms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokedex.form')),
                ('game_indices', models.ManyToManyField(to='pokedex.gameindex')),
                ('location_area_encounters', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokedex.locationarea')),
                ('moves', models.ManyToManyField(to='pokedex.move')),
                ('past_types', models.ManyToManyField(related_name='past_pokemon', to='pokedex.type')),
                ('species', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pokemon', to='pokedex.type')),
                ('sprites', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pokemon_sprites', to='pokedex.type')),
                ('stats', models.ManyToManyField(to='pokedex.stat')),
                ('types', models.ManyToManyField(related_name='type', to='pokedex.type')),
            ],
        ),
    ]
