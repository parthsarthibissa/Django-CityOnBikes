# Generated by Django 2.2 on 2020-06-24 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike', '0008_auto_20200623_1354'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookingdetails',
            old_name='booked_date',
            new_name='booking_date',
        ),
        migrations.AlterField(
            model_name='bookingdetails',
            name='destination',
            field=models.TextField(default='', max_length=300),
        ),
    ]
