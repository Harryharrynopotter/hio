# Generated by Django 2.2.3 on 2019-07-21 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bypass', '0004_auto_20190721_0420'),
    ]

    operations = [
        migrations.AddField(
            model_name='bypass',
            name='bot_name',
            field=models.CharField(max_length=10, null=True, verbose_name='机器人名'),
        ),
        migrations.AddField(
            model_name='task',
            name='bot_name',
            field=models.CharField(max_length=10, null=True, verbose_name='机器人名'),
        ),
    ]