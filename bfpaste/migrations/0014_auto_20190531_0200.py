# Generated by Django 2.2.1 on 2019-05-30 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bfpaste', '0013_auto_20190531_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paste',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Publising date'),
        ),
    ]
