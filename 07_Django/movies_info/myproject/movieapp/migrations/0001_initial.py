# Generated by Django 5.2 on 2025-04-21 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieMod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mnane', models.CharField(max_length=20)),
                ('rdate', models.DateField()),
                ('hero', models.CharField(max_length=50)),
                ('heroine', models.CharField(max_length=50)),
                ('director', models.CharField()),
                ('lang', models.CharField(max_length=20)),
                ('rating', models.FloatField()),
            ],
        ),
    ]
