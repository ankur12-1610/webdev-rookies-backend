# Generated by Django 3.2.6 on 2021-08-31 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20210831_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='score',
            field=models.CharField(max_length=255),
        ),
    ]
