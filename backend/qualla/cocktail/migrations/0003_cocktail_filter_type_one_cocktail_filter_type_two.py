# Generated by Django 4.1.1 on 2022-11-07 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cocktail', '0002_auto_20221026_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='cocktail',
            name='filter_type_one',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='cocktail',
            name='filter_type_two',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
