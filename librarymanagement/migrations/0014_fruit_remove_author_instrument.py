# Generated by Django 4.0.2 on 2022-03-11 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarymanagement', '0013_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fruit',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='author',
            name='instrument',
        ),
    ]
