# Generated by Django 2.2.7 on 2020-02-18 15:21

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_no', models.IntegerField(validators=[django.core.validators.MinValueValidator(10000), django.core.validators.MaxValueValidator(20000)],default=0)),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=250)),
                ('image', models.ImageField(default='pics/default.png', upload_to='profile_pics')),
                ('roll_no', models.IntegerField(default=0)),
                ('address', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
