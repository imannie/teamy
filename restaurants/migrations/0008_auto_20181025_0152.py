# Generated by Django 2.1.2 on 2018-10-25 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0007_auto_20181024_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurants_info',
            name='selected',
            field=models.CharField(default='0', max_length=300),
        ),
    ]
