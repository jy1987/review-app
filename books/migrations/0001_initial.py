# Generated by Django 2.2.5 on 2021-06-02 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('people', '0002_auto_20210602_2325'),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=60)),
                ('year', models.DateField()),
                ('cover_image', models.ImageField(upload_to='')),
                ('rating', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='categories.Category')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='people.Person')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
