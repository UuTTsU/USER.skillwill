# Generated by Django 4.2.11 on 2024-04-04 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfields',
            name='age',
            field=models.IntegerField(),
        ),
    ]