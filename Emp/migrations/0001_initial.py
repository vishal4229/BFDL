# Generated by Django 3.2.4 on 2021-06-14 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('emp_id', models.IntegerField(max_length=20, primary_key=True, serialize=False)),
                ('emp_name', models.CharField(max_length=264)),
                ('emp_email', models.EmailField(max_length=264, unique=True)),
                ('emp_password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Emp_Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('fb_url', models.URLField(blank=True)),
                ('lk_url', models.URLField(blank=True)),
            ],
        ),
    ]
