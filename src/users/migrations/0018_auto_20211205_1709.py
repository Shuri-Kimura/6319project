# Generated by Django 3.2.8 on 2021-12-05 08:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_alter_tcom_tcom_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='texts',
            name='image1',
            field=models.ImageField(default=datetime.datetime(2021, 12, 5, 8, 9, 19, 965364, tzinfo=utc), upload_to='src/textpage/static/textpage/image1/', verbose_name='商品画像１'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='texts',
            name='title',
            field=models.TextField(max_length=50),
        ),
    ]
