# Generated by Django 2.1.2 on 2018-10-19 00:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_auto_20181019_0012'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurants_info',
            old_name='check',
            new_name='hold',
        ),
    ]
