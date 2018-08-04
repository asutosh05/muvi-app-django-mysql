# Generated by Django 2.0.7 on 2018-08-04 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('releaseDate', models.DateTimeField()),
                ('genre', models.CharField(blank=True, max_length=120, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.CharField(blank=True, max_length=500, null=True)),
                ('geoRights', models.CharField(blank=True, max_length=500, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=3, max_digits=50, null=True)),
                ('currency', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
    ]