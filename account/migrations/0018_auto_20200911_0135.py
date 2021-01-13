# Generated by Django 2.2.12 on 2020-09-10 20:05

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0017_profile_present_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='document10',
            field=models.FileField(blank=True, null=True, upload_to='documents/user_documents/10marksheets', validators=[account.models.file_size1]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='document12',
            field=models.FileField(blank=True, null=True, upload_to='documents/user_documents/12marksheets', validators=[account.models.file_size1]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='document_last_sem',
            field=models.FileField(blank=True, null=True, upload_to='documents/user_documents/last_marksheets', validators=[account.models.file_size1]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='father_id',
            field=models.FileField(blank=True, null=True, upload_to='documents/user_documents/father_id', validators=[account.models.file_size1]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='pics/profile_pics/default.png', upload_to='pics/profile_pics', validators=[account.models.file_size1]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='student_id',
            field=models.FileField(blank=True, null=True, upload_to='documents/user_documents/student_id', validators=[account.models.file_size1]),
        ),
    ]
