# Generated by Django 3.1.4 on 2020-12-23 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_channel_keyword'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
        migrations.AlterField(
            model_name='channel',
            name='facebook',
            field=models.URLField(default=None),
        ),
        migrations.AlterField(
            model_name='channel',
            name='instagram',
            field=models.URLField(default=None),
        ),
        migrations.AlterField(
            model_name='channel',
            name='linkedin',
            field=models.URLField(default=None),
        ),
        migrations.AlterField(
            model_name='channel',
            name='twitter',
            field=models.URLField(default=None),
        ),
    ]
