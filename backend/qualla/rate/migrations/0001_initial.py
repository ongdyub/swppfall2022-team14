# Generated by Django 4.1.2 on 2022-11-12 16:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cocktail', '0006_merge_20221107_1800'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cocktail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rate_set', to='cocktail.cocktail')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rate_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='rate',
            constraint=models.UniqueConstraint(fields=('cocktail', 'user'), name='unique_cocktail_user_combination'),
        ),
    ]