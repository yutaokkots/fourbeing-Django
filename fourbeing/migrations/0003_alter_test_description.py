# Generated by Django 4.2 on 2023-05-06 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fourbeing', '0002_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='description',
            field=models.CharField(max_length=100),
        ),
    ]