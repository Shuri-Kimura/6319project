# Generated by Django 3.2.7 on 2021-11-06 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20211105_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='texts',
            name='title',
            field=models.TextField(default='出品サンプル', max_length=50),
        ),
    ]
