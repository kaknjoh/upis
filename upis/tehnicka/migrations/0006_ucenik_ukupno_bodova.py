# Generated by Django 2.2.9 on 2020-01-04 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tehnicka', '0005_takmicenje'),
    ]

    operations = [
        migrations.AddField(
            model_name='ucenik',
            name='ukupno_bodova',
            field=models.FloatField(default='0'),
        ),
    ]