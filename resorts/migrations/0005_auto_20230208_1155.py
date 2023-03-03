# Generated by Django 3.2.17 on 2023-02-08 11:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resorts', '0004_resort_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='rating',
        ),
        migrations.AddField(
            model_name='rating',
            name='star_rating',
            field=models.ManyToManyField(blank=True, related_name='resort_rating', to=settings.AUTH_USER_MODEL),
        ),
    ]