# Generated by Django 3.2.8 on 2021-11-13 01:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20211113_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='texts',
            name='text_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
