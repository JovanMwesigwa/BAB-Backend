# Generated by Django 3.0.5 on 2020-11-18 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0023_auto_20201109_1942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_likes',
        ),
        migrations.AlterField(
            model_name='likepost',
            name='liked_post',
            field=models.ManyToManyField(related_name='likes', to='post.Post'),
        ),
    ]