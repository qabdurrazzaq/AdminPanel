# Generated by Django 3.2 on 2021-05-06 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userfeatures', '0003_alter_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='mobile_no',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
