# Generated by Django 2.2.5 on 2021-06-07 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20210603_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(blank=True, upload_to='book_photos'),
        ),
    ]
