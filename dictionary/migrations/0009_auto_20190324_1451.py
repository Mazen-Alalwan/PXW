# Generated by Django 2.1.3 on 2019-03-24 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0008_auto_20190324_1439'),
    ]

    operations = [
        migrations.RenameField(
            model_name='word',
            old_name='derivation_symbol1',
            new_name='derivation1_symbol',
        ),
        migrations.RenameField(
            model_name='word',
            old_name='derivation_symbol2',
            new_name='derivation2_symbol',
        ),
        migrations.RenameField(
            model_name='word',
            old_name='derivation_symbol3',
            new_name='derivation3_symbol',
        ),
        migrations.RenameField(
            model_name='word',
            old_name='derivation_symbol4',
            new_name='derivation4_symbol',
        ),
        migrations.RenameField(
            model_name='word',
            old_name='derivation_symbol5',
            new_name='derivation5_symbol',
        ),
    ]