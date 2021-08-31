# Generated by Django 3.2.6 on 2021-08-31 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_auto_20210831_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='assignment_link',
            field=models.URLField(default='None', max_length=255),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='classroom_link',
            field=models.URLField(default='None', max_length=255),
        ),
    ]