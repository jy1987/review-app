# Generated by Django 2.2.5 on 2021-06-02 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('abstractitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='categories.AbstractItem')),
                ('kind', models.CharField(choices=[('book', 'Book'), ('movie', 'Movie'), ('both', 'Both')], default='Both', max_length=10)),
            ],
            options={
                'abstract': False,
            },
            bases=('categories.abstractitem',),
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('abstractitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='categories.AbstractItem')),
            ],
            options={
                'abstract': False,
            },
            bases=('categories.abstractitem',),
        ),
    ]
