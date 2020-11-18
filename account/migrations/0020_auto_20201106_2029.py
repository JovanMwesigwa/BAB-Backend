# Generated by Django 3.0.5 on 2020-11-06 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0019_userfollowing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfollowing',
            name='followed',
            field=models.ManyToManyField(related_name='followers', to='account.Profile'),
        ),
        migrations.AlterField(
            model_name='userfollowing',
            name='following',
            field=models.ManyToManyField(related_name='user_following', to='account.Profile'),
        ),
    ]
