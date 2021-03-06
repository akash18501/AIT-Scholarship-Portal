# Generated by Django 2.2.12 on 2020-09-09 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0012_current_session'),
    ]

    operations = [
        migrations.AddField(
            model_name='application_table',
            name='applied_scholarship_form',
            field=models.FileField(blank=True, null=True, upload_to='applications/applied_scholarship_form'),
        ),
        migrations.AddField(
            model_name='scholarship',
            name='scholarship_form',
            field=models.FileField(default='documents/scholarship_form/default_scholarship_form.pdf', upload_to='documents/scholarship_form/'),
        ),
    ]
