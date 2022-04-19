# Generated by Django 4.0.4 on 2022-04-18 10:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0003_remove_likes_like_likes_owner_alter_likes_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likes',
            name='owner',
        ),
        migrations.AddField(
            model_name='likes',
            name='owner',
            field=models.ManyToManyField(blank=True, related_name='like', to=settings.AUTH_USER_MODEL),
        ),
    ]
