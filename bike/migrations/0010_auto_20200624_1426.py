# Generated by Django 2.2 on 2020-06-24 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike', '0009_auto_20200624_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingdetails',
            name='destination',
            field=models.SlugField(),
        ),
    ]
