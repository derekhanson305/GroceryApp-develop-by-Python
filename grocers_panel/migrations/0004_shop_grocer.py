# Generated by Django 3.2.3 on 2021-12-19 16:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('grocers_panel', '0003_auto_20211217_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='grocer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
