# Generated by Django 2.1.3 on 2019-03-24 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0003_word_root'),
    ]

    operations = [
        migrations.RenameField(
            model_name='word',
            old_name='main',
            new_name='meaning',
        ),
    ]