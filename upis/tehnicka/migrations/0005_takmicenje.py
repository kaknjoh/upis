# Generated by Django 2.2.9 on 2020-01-02 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tehnicka', '0004_ucenik_smjer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Takmicenje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vrsta_takmicenja', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name_plural': 'Takmicenja',
            },
        ),
    ]