# Generated by Django 3.2.3 on 2022-07-18 20:39
import uuid
from django.db import migrations, models


def create_food_id(apps, schema_editor):
    MyModel = apps.get_model('grocery_api', 'food')
    food_id = 1
    for my_model in MyModel.objects.all().iterator(chunk_size=50):
        my_model.food_pk = food_id
        my_model.save()
        food_id += 1


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_api', '0006_food_food_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='food_pk',
            field=models.IntegerField(editable=False, null=True),
            preserve_default=False,
        ),
        migrations.RunPython(create_food_id, reverse_code=migrations.RunPython.noop),
        migrations.AlterField(
            model_name='food',
            name='food_pk',
            field=models.IntegerField(editable=False, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='food',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=False),
        ),
    ]
