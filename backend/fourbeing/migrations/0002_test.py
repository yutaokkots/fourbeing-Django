# Generated by Django 4.2 on 2023-05-06 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fourbeing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=20)),
            ],
        ),
    ]
