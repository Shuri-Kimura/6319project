# Generated by Django 3.2.8 on 2021-12-15 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0027_alter_messages_eval_flag'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='reading_flag',
            field=models.BooleanField(default=True),
        ),
    ]
