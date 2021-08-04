# Generated by Django 3.1.4 on 2021-07-11 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20201224_1058'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='video',
            name='channel_id',
        ),
        migrations.RemoveField(
            model_name='video',
            name='channel_link',
        ),
        migrations.RemoveField(
            model_name='video',
            name='channel_name',
        ),
        migrations.RemoveField(
            model_name='video',
            name='email',
        ),
        migrations.RemoveField(
            model_name='video',
            name='subscriber',
        ),
        migrations.RemoveField(
            model_name='video',
            name='total_video_count',
        ),
        migrations.RemoveField(
            model_name='video',
            name='total_view_count',
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_id', models.CharField(max_length=20, null=True)),
                ('channel_name', models.CharField(max_length=200, null=True)),
                ('channel_link', models.URLField(null=True)),
                ('email', models.EmailField(max_length=200, null=True)),
                ('total_view_count', models.IntegerField(blank=True, null=True)),
                ('subscriber', models.IntegerField(blank=True, null=True)),
                ('total_video_count', models.IntegerField(blank=True, null=True)),
                ('keyword', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.keyword')),
            ],
        ),
        migrations.AddField(
            model_name='video',
            name='channel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.channel'),
        ),
        migrations.AlterField(
            model_name='video',
            name='keyword',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.keyword'),
        ),
    ]
