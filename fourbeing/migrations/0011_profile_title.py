# Generated by Django 4.2 on 2023-05-11 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fourbeing', '0010_post_created_profile_location_profile_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='title',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
    ]
