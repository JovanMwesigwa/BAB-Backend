# Generated by Django 3.0.5 on 2020-10-19 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_sponsoredprofiles'),
    ]

    operations = [
        migrations.CreateModel(
            name='SponsoredProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sponsored_profile', models.ManyToManyField(to='account.Profile')),
            ],
        ),
        migrations.DeleteModel(
            name='SponsoredProfiles',
        ),
    ]
