# Generated by Django 4.1.2 on 2022-11-12 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]