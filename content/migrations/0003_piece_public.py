# Generated by Django 4.1.3 on 2022-12-04 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20221202_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='piece',
            name='public',
            field=models.BooleanField(default=True),
        ),
    ]
