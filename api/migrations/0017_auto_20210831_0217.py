# Generated by Django 3.2.6 on 2021-08-30 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20210828_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='classroom_link',
            field=models.CharField(default='None', max_length=255),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='score',
            field=models.CharField(default='ungraded', max_length=255),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='classroom_color',
            field=models.CharField(default='blue', max_length=255),
        ),
    ]
