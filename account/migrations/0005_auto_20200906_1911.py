# Generated by Django 3.0.5 on 2020-09-06 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20200906_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.ProfileType'),
        ),
    ]
