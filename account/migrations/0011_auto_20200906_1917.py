# Generated by Django 3.0.5 on 2020-09-06 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20200906_1916'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.ProfileType'),
        ),
    ]
