# Generated by Django 2.1.2 on 2018-12-14 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('requestHandler', '0010_auto_20181214_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemsettings',
            name='DefaultSong',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='requestHandler.Song'),
        ),
    ]
