# Generated by Django 2.2.5 on 2021-06-02 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20210602_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='preference',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='categories.Category'),
        ),
    ]