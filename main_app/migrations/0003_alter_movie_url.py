# Generated by Django 4.0.6 on 2022-07-25 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_movie_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='url',
            field=models.FileField(upload_to='photo_file/'),
        ),
    ]