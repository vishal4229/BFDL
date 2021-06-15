# Generated by Django 3.2.4 on 2021-06-14 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Emp', '0004_emp_emp_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='emp_profile',
            name='emp_pro_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Emp.emp'),
        ),
        migrations.AlterField(
            model_name='emp_profile',
            name='fb_url',
            field=models.URLField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='emp_profile',
            name='lk_url',
            field=models.URLField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='emp_profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='', upload_to='profile_pics'),
        ),
    ]