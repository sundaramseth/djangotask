# Generated by Django 2.2.1 on 2019-06-01 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20190601_0911'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField(verbose_name='D.O.B')),
            ],
        ),
        migrations.DeleteModel(
            name='HolidayTimeForm',
        ),
    ]
