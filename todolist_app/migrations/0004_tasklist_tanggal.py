# Generated by Django 2.2.5 on 2022-09-29 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0003_auto_20200509_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasklist',
            name='tanggal',
            field=models.DateField(default='2022-09-01'),
        ),
    ]
