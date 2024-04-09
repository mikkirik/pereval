# Generated by Django 5.0.4 on 2024-04-09 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pereval',
            old_name='coord',
            new_name='coords',
        ),
        migrations.AlterField(
            model_name='level',
            name='autumn',
            field=models.CharField(choices=[('1А', '1А'), ('1Б', '1Б'), ('2А', '2А'), ('2Б', '2Б'), ('3А', '3А'), ('3Б', '3Б')], default='1А', max_length=2),
        ),
        migrations.AlterField(
            model_name='level',
            name='spring',
            field=models.CharField(choices=[('1А', '1А'), ('1Б', '1Б'), ('2А', '2А'), ('2Б', '2Б'), ('3А', '3А'), ('3Б', '3Б')], default='1А', max_length=2),
        ),
        migrations.AlterField(
            model_name='level',
            name='summer',
            field=models.CharField(choices=[('1А', '1А'), ('1Б', '1Б'), ('2А', '2А'), ('2Б', '2Б'), ('3А', '3А'), ('3Б', '3Б')], default='1А', max_length=2),
        ),
        migrations.AlterField(
            model_name='level',
            name='winter',
            field=models.CharField(choices=[('1А', '1А'), ('1Б', '1Б'), ('2А', '2А'), ('2Б', '2Б'), ('3А', '3А'), ('3Б', '3Б')], default='1А', max_length=2),
        ),
    ]