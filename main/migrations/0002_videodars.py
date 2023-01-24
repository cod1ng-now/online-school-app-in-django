# Generated by Django 4.0.3 on 2022-05-14 03:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoDars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=150)),
                ('rasm', models.ImageField(upload_to='video_darslar/rasmlar')),
                ('izoh', models.TextField()),
                ('video', models.FileField(upload_to='video_darslar/video')),
                ('playlisti', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.playlist')),
            ],
        ),
    ]
