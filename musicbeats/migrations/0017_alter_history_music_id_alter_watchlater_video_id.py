# Generated by Django 4.0 on 2021-12-30 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicbeats', '0016_alter_history_music_id_alter_song_movie_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='music_id',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='watchlater',
            name='video_id',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
    ]
