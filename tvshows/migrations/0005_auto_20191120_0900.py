# Generated by Django 2.2.7 on 2019-11-20 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvshows', '0004_episode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='episodeName',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]