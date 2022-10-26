# Generated by Django 3.2.6 on 2022-10-26 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cocktail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('image', models.CharField(max_length=500)),
                ('introduction', models.CharField(max_length=500)),
                ('recipe', models.CharField(max_length=1000)),
                ('ABV', models.FloatField()),
                ('price_per_glass', models.FloatField()),
                ('type', models.CharField(choices=[('ST', 'Standard Cocktail'), ('CS', 'Custom Cocktail')], max_length=2)),
                ('author_id', models.IntegerField(default=None, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddConstraint(
            model_name='cocktail',
            constraint=models.CheckConstraint(check=models.Q(models.Q(('type', 'CS'), models.Q(('author_id', None), _negated=True)), ('type', 'ST'), _connector='OR'), name='custom cocktail should have author'),
        ),
    ]