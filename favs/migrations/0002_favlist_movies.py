# Generated by Django 2.2.5 on 2021-06-07 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0001_initial'),
        ('favs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='favlist',
            name='movies',
            field=models.ManyToManyField(related_name='favs', to='movies.Movie'),
        ),
    ]
