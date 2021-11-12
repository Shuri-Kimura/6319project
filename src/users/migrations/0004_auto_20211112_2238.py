# Generated by Django 3.2.8 on 2021-11-12 13:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_texts_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='texts',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='src/textpage/static/textpage/image1/', verbose_name='商品画像１'),
        ),
        migrations.AlterField(
            model_name='texts',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='src/textpage/static/textpage/image2/', verbose_name='商品画像２'),
        ),
        migrations.AlterField(
            model_name='texts',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='src/textpage/static/textpage/image3/', verbose_name='商品画像３'),
        ),
        migrations.AlterField(
            model_name='texts',
            name='text_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
