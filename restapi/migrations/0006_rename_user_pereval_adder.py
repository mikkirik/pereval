# Generated by Django 5.0.4 on 2024-04-09 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0005_alter_image_pereval'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pereval',
            old_name='user',
            new_name='adder',
        ),
    ]
