# Generated by Django 3.2.8 on 2021-11-13 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_texts_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='texts',
            name='text_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
