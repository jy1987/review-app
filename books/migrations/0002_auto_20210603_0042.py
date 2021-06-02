# Generated by Django 2.2.5 on 2021-06-02 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_remove_category_genre'),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='category',
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='books', to='categories.Genre'),
        ),
    ]
