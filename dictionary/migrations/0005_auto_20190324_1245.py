# Generated by Django 2.1.3 on 2019-03-24 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0004_auto_20190324_1242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='meaning',
        ),
        migrations.AddField(
            model_name='word',
            name='meaning1',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='word',
            name='meaning2',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='word',
            name='meaning3',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='word',
            name='meaning4',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='word',
            name='meaning5',
            field=models.CharField(default='', max_length=20),
        ),
    ]
