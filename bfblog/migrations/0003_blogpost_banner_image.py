# Generated by Django 2.2.1 on 2019-05-31 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bfblog', '0002_auto_20190531_0208'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='banner_image',
            field=models.ImageField(default='default.jpg', upload_to='postimages/', verbose_name='Post image'),
            preserve_default=False,
        ),
    ]
