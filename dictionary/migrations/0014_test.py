# Generated by Django 2.1.3 on 2019-03-30 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0013_auto_20190324_1543'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(default='', max_length=20)),
            ],
        ),
    ]