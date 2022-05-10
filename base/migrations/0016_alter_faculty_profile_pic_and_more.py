# Generated by Django 4.0.4 on 2022-05-10 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_alter_student_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='profile_pic',
            field=models.ImageField(blank=True, default='base/static/base/images/default_profile_pic.jpg', upload_to='base/static/base/images'),
        ),
        migrations.AlterField(
            model_name='nonteaching',
            name='profile_pic',
            field=models.ImageField(blank=True, default='base/static/base/images/default_profile_pic.jpg', upload_to='base/static/base/images'),
        ),
    ]
