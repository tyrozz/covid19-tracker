# Generated by Django 3.1.7 on 2021-10-17 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0005_auto_20211017_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='country_code',
            field=models.IntegerField(blank=True, help_text='Unique code for a country. For example Belgium:56', null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='location_code',
            field=models.IntegerField(blank=True, help_text='Unique code for each location. For example Brussels-Belgium:5602, East Flanders-Belgium:5603', null=True),
        ),
    ]