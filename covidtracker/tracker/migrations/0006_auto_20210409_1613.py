# Generated by Django 3.1.7 on 2021-04-09 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0005_auto_20210409_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='longitute',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=12, null=True),
        ),
    ]
