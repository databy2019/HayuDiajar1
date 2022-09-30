# Generated by Django 2.2.5 on 2022-09-29 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0004_tasklist_tanggal'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasklist',
            name='cara',
            field=models.CharField(default='Duduk', max_length=25),
        ),
        migrations.AddField(
            model_name='tasklist',
            name='durasi',
            field=models.IntegerField(default=30),
        ),
        migrations.AddField(
            model_name='tasklist',
            name='jam',
            field=models.TimeField(default='20:30:30'),
        ),
        migrations.AddField(
            model_name='tasklist',
            name='negatif',
            field=models.TextField(default='None', max_length=255),
        ),
        migrations.AddField(
            model_name='tasklist',
            name='nilai',
            field=models.FloatField(default=90.0, max_length=4),
        ),
        migrations.AddField(
            model_name='tasklist',
            name='pelajaran',
            field=models.CharField(default='Matematika', max_length=25),
        ),
        migrations.AddField(
            model_name='tasklist',
            name='positif',
            field=models.TextField(default='None', max_length=255),
        ),
        migrations.AddField(
            model_name='tasklist',
            name='waktu',
            field=models.CharField(default='Malam', max_length=10),
        ),
        migrations.AlterField(
            model_name='tasklist',
            name='done',
            field=models.BooleanField(default=True),
        ),
    ]
