# Generated by Django 3.2.8 on 2021-12-15 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0030_alter_tcom_exhibitor_or_all'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tcom',
            name='exhibitor_or_all',
            field=models.BooleanField(default=False),
        ),
    ]
