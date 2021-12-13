# Generated by Django 3.2.8 on 2021-12-13 18:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_classes_credit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='credit',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
