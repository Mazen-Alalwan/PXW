# Generated by Django 2.1.3 on 2019-03-12 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Dictionary',
            new_name='Word',
        ),
    ]
