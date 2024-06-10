# Generated by Django 5.0.6 on 2024-06-07 13:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Service_Apointments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateField(null=True, verbose_name='Datum')),
                ('levertijd', models.CharField(max_length=47, null=True, verbose_name='Levertijd van tot')),
                ('sity', models.CharField(max_length=47, verbose_name='Plaats')),
                ('postcode', models.CharField(max_length=14)),
                ('ordernr', models.CharField(max_length=47, verbose_name='Order NR')),
                ('price', models.CharField(max_length=47, null=True, verbose_name='Prijs')),
                ('client', models.CharField(max_length=100, verbose_name='Naam')),
                ('telefon', models.CharField(max_length=47, verbose_name='Telefoon')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Gebruiker')),
            ],
        ),
    ]
