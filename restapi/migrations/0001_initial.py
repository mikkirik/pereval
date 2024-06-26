# Generated by Django 5.0.4 on 2024-04-07 19:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('height', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('data', models.ImageField(upload_to='')),
                ('add_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winter', models.CharField(choices=[('1A', '1А'), ('1B', '1Б'), ('2A', '2А'), ('2B', '2Б'), ('3A', '3А'), ('3B', '3Б')], default='1A', max_length=2)),
                ('summer', models.CharField(choices=[('1A', '1А'), ('1B', '1Б'), ('2A', '2А'), ('2B', '2Б'), ('3A', '3А'), ('3B', '3Б')], default='1A', max_length=2)),
                ('autumn', models.CharField(choices=[('1A', '1А'), ('1B', '1Б'), ('2A', '2А'), ('2B', '2Б'), ('3A', '3А'), ('3B', '3Б')], default='1A', max_length=2)),
                ('spring', models.CharField(choices=[('1A', '1А'), ('1B', '1Б'), ('2A', '2А'), ('2B', '2Б'), ('3A', '3А'), ('3B', '3Б')], default='1A', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=20)),
                ('fam', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('otc', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Pereval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beauty_title', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('other_titles', models.CharField(max_length=255)),
                ('connect', models.TextField()),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('new', 'новый'), ('pending', 'на модерации'), ('accepted', 'модерация успешна'), ('rejected', 'информация не принята')], default='new', max_length=30)),
                ('coord', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='restapi.coords')),
                ('level', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='restapi.level')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.user')),
            ],
        ),
        migrations.CreateModel(
            name='PerevalImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.image')),
                ('pereval', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.pereval')),
            ],
        ),
    ]
