# Generated by Django 3.0.7 on 2021-08-28 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20210828_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='classroom_color',
            field=models.BooleanField(choices=[('', 'Custom Profile Picture'), ('1', 'Blue-theme'), ('2', 'Red-theme'), ('3', 'Violet-theme'), ('4', 'Green-theme')], default=False),
        ),
    ]
