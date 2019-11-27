# Generated by Django 2.2.7 on 2019-11-20 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medium', models.CharField(max_length=200)),
                ('original', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('episodeOrder', models.IntegerField()),
                ('premiereDate', models.DateField()),
                ('endDate', models.DateField()),
                ('webChannel', models.CharField(max_length=200)),
                ('summary', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('seriesURL', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=20)),
                ('runtime', models.IntegerField()),
                ('premiered', models.DateField()),
                ('officialSite', models.CharField(max_length=200)),
                ('weight', models.IntegerField()),
                ('summary', models.TextField()),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tvshows.Image')),
            ],
        ),
    ]
