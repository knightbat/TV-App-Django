# Generated by Django 2.2.7 on 2019-11-20 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tvshows', '0007_auto_20191120_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='season',
            name='series',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seasons', to='tvshows.Series'),
        ),
    ]