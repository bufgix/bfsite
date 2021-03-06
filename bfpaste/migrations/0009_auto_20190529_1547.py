# Generated by Django 2.2.1 on 2019-05-29 12:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bfpaste', '0008_auto_20190529_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paste',
            name='lang',
            field=models.CharField(choices=[('c', 'C'), ('c++', 'C++'), ('css', 'CSS'), ('java', 'Java'), ('javascript', 'JavaScript'), ('python', 'Python')], max_length=100),
        ),
        migrations.AlterField(
            model_name='paste',
            name='paste_id',
            field=models.CharField(default='10066dc51c7039f34f15', max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='paste',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 29, 12, 47, 47, 119764, tzinfo=utc), verbose_name='Publising date'),
        ),
    ]
