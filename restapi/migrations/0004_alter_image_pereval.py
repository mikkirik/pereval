# Generated by Django 5.0.4 on 2024-04-09 15:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0003_image_pereval_delete_perevalimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='pereval',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.pereval'),
        ),
    ]
