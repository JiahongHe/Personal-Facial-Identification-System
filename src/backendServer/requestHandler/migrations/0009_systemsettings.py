# Generated by Django 2.1.2 on 2018-12-14 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requestHandler', '0008_auto_20181126_0212'),
    ]

    operations = [
        migrations.CreateModel(
            name='SystemSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DefaultBehavior', models.CharField(choices=[('RandomSong', 'RandomSong'), ('DefaultSong', 'DefaultSong'), ('Voice', 'Voice'), ('Beep', 'Beep')], default='DefaultSong', max_length=9)),
            ],
        ),
    ]