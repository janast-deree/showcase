# Generated by Django 3.2.8 on 2022-12-02 13:12

import content.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=280)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=280)),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to=content.models.image_file_name)),
                ('art', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='artists', to='content.art')),
            ],
        ),
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=280)),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to=content.models.image_file_name)),
                ('artists', models.ManyToManyField(blank=True, default=None, null=True, related_name='exhibitions', to='content.Artist')),
            ],
        ),
    ]