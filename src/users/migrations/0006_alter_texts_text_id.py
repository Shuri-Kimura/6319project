# Generated by Django 3.2.8 on 2021-11-12 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_texts_text_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='texts',
            name='text_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
