# Generated by Django 2.2.5 on 2021-06-15 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='movie_photos'),
        ),
    ]
