# Generated by Django 2.2.7 on 2020-06-17 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0007_auto_20200518_2356'),
    ]

    operations = [
        migrations.AddField(
            model_name='scholarship',
            name='status',
            field=models.IntegerField(blank=True, default=2, null=True),
        ),
    ]
