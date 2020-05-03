# Generated by Django 3.0.5 on 2020-04-29 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0003_country_users'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'city', 'verbose_name_plural': 'cities'},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name': 'country', 'verbose_name_plural': 'countries'},
        ),
        migrations.AlterModelOptions(
            name='symbol',
            options={'verbose_name': 'flag', 'verbose_name_plural': 'flags'},
        ),
    ]
