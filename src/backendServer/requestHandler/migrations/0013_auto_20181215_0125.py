# Generated by Django 2.1.4 on 2018-12-15 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requestHandler', '0012_auto_20181214_2136'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SystemSettings',
            new_name='SystemSetting',
        ),
    ]