# Generated by Django 2.2.7 on 2019-11-20 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tvshows', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='season',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tvshows.Image'),
        ),
        migrations.AlterField(
            model_name='series',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tvshows.Image'),
        ),
    ]
