# Generated by Django 3.2.8 on 2021-12-15 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_auto_20211215_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='Eval_flag',
            field=models.BooleanField(default=True),
        ),
    ]