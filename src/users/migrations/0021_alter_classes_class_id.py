# Generated by Django 3.2.8 on 2021-12-13 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_target'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='class_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
