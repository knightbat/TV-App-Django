# Generated by Django 2.2.7 on 2019-11-20 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvshows', '0005_auto_20191120_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='season',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
