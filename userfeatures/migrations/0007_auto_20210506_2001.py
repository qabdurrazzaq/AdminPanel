# Generated by Django 3.2 on 2021-05-06 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userfeatures', '0006_auto_20210506_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='add_user',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='del_user',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='edit_user',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='user_stats',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='view_user',
            field=models.BooleanField(default=False),
        ),
    ]
