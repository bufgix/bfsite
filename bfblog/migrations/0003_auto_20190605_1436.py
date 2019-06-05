# Generated by Django 2.2.1 on 2019-06-05 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bfblog', '0002_auto_20190604_1418'),
    ]

    operations = [
        migrations.CreateModel(
            name='BloTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.AddField(
            model_name='blogpost',
            name='tags',
            field=models.ManyToManyField(to='bfblog.BloTags'),
        ),
    ]
