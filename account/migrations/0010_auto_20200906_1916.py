# Generated by Django 3.0.5 on 2020-09-06 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_auto_20200906_1916'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile_type',
        ),
        migrations.DeleteModel(
            name='ProfileType',
        ),
    ]
