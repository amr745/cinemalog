# Generated by Django 4.0.6 on 2022-07-24 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('synopsis', models.TextField(max_length=250)),
                ('date', models.DateField(verbose_name='feeding date')),
                ('rating', models.CharField(max_length=10)),
                ('genre', models.CharField(choices=[('D', 'Drama'), ('T', 'Thriller'), ('R', 'Romance'), ('A', 'Action'), ('C', 'Comedy'), ('H', 'Horror'), ('S', 'Science Fiction'), ('F', 'Fantacy')], default='D', max_length=1)),
                ('url', models.CharField(max_length=200)),
            ],
        ),
    ]