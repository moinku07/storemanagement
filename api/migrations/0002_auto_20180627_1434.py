# Generated by Django 2.0.6 on 2018-06-27 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='fb_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='main_picture',
            field=models.ImageField(blank=True, null=True, upload_to='media/uploads/stores/'),
        ),
    ]
