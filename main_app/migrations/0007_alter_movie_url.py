# Generated by Django 4.0.6 on 2022-07-26 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_movie_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='url',
            field=models.FileField(upload_to=''),
        ),
    ]
