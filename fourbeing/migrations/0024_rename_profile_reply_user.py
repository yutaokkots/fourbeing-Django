# Generated by Django 4.2 on 2023-05-13 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fourbeing', '0023_alter_post_profile_alter_reply_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reply',
            old_name='profile',
            new_name='user',
        ),
    ]
