# Generated by Django 5.0.3 on 2024-03-26 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plumb_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='img',
            field=models.ImageField(upload_to='media/movies/'),
        ),
    ]
