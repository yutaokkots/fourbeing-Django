# Generated by Django 4.2 on 2023-05-13 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fourbeing', '0019_reply_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='love',
            field=models.IntegerField(default=0),
        ),
    ]
