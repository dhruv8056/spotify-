# Generated by Django 4.0 on 2021-12-30 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('musicbeats', '0017_alter_history_music_id_alter_watchlater_video_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='History2',
            fields=[
                ('hist_id2', models.AutoField(primary_key=True, serialize=False)),
                ('musi2c_id', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('user2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]