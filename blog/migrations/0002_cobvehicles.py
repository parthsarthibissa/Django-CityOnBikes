# Generated by Django 2.2 on 2020-06-16 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='COBVehicles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_name', models.SlugField(default='')),
                ('category_name', models.SlugField(default='', max_length=15)),
                ('price', models.SlugField(default='', max_length=30)),
            ],
        ),
    ]
