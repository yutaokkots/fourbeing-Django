# Generated by Django 4.2 on 2023-05-11 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fourbeing', '0005_remove_profile_id_alter_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='username',
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile',
            field=models.CharField(max_length=300),
        ),
    ]
