# Generated by Django 2.0.6 on 2018-06-27 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180627_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='storebranch',
            name='phone',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Phone'),
        ),
    ]
